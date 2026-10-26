"""Build web images for the Cocares page from a JSON manifest.

Usage:
    python scripts/build-cocares-images.py                 # all entries
    python scripts/build-cocares-images.py name1 name2     # only these "out" names
    python scripts/build-cocares-images.py --manifest other.json

Manifest (scripts/cocares-images.json):
    {
      "entries": [
        {
          "src": "rainbow/rainbow-detail-01.jpg",   # relative to SRC_DIR
          "out": "rainbow-detail",                   # -> docs/media/images/cocares/<out>.jpg/.webp
          "crop": [0.1, 0.0, 0.9, 1.0],             # x0, y0, x1, y1 as fractions, or null
          "aspect": "3:4",                          # "2:3" | "3:4" | "1:1" | any "w:h" | null
          "width": 900,                              # output pixel width (never upscaled)
          "fix": {"wb": true, "shadow": 0.9, "exposure": -0.2, "warm": 0.03}   # optional
        }
      ]
    }

Pipeline per entry: EXIF transpose -> crop box (if given) -> centre-crop to
aspect (if given; applied after the crop box, so a box can be loose) ->
Lanczos resize to width -> tonal fixes (in order: wb, exposure, shadow, warm) -> light unsharp mask -> write
JPEG (q88, progressive) and WebP (q82). Metadata is stripped.

Fixes:
    wb        grey-world on the brightest 2 % of pixels, gains clamped 0.8-1.25
    shadow    luminance gamma (< 1 lifts shadows, > 1 deepens), applied unconditionally
    exposure  in stops (EV): pixel values are multiplied by 2**exposure
    warm      colour temperature nudge: R *= 1 + warm, B *= 1 - warm (0.03 is mild;
              negative cools)

"sharpen": false skips the unsharp mask (for sources the phone already over-sharpened).
Keys starting with "_" anywhere in the manifest are ignored (use them for notes).
Originals are never modified. Re-running overwrites outputs (idempotent).
"""
import argparse
import json
import os
import sys

import numpy as np
from PIL import Image, ImageFilter, ImageOps

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
SRC_DIR = os.path.normpath(os.path.join(ROOT, "..", "Cocars", "Photos"))
OUT_DIR = os.path.join(ROOT, "docs", "media", "images", "cocares")
DEFAULT_MANIFEST = os.path.join(HERE, "cocares-images.json")

JPEG_QUALITY = 88
WEBP_QUALITY = 82

WB_BRIGHT_FRACTION = 0.02
WB_GAIN_MIN, WB_GAIN_MAX = 0.8, 1.25

# Light sharpening after downscale
USM_RADIUS = 0.8
USM_PERCENT = 40
USM_THRESHOLD = 2


def luminance(rgb):
    return 0.299 * rgb[..., 0] + 0.587 * rgb[..., 1] + 0.114 * rgb[..., 2]


def white_balance(rgb):
    lum = luminance(rgb)
    thr = np.quantile(lum, 1.0 - WB_BRIGHT_FRACTION)
    means = rgb[lum >= thr].mean(axis=0)
    gains = np.clip(means.mean() / np.maximum(means, 1e-6), WB_GAIN_MIN, WB_GAIN_MAX)
    return np.clip(rgb * gains, 0, 255)


def shadow_gamma(rgb, gamma):
    lum = np.maximum(luminance(rgb), 1e-3)
    new = 255.0 * (lum / 255.0) ** gamma
    return np.clip(rgb * (new / lum)[..., None], 0, 255)


def exposure(rgb, ev):
    return np.clip(rgb * (2.0 ** ev), 0, 255)


def warm(rgb, amount):
    gains = np.array([1.0 + amount, 1.0, 1.0 - amount], dtype=np.float32)
    return np.clip(rgb * gains, 0, 255)


def parse_aspect(s):
    w, h = (float(v) for v in s.split(":"))
    if w <= 0 or h <= 0:
        raise ValueError(f"bad aspect {s!r}")
    return w / h


def crop_fraction(img, box):
    x0, y0, x1, y1 = box
    if not (0 <= x0 < x1 <= 1 and 0 <= y0 < y1 <= 1):
        raise ValueError(f"crop box out of range: {box}")
    W, H = img.size
    return img.crop((round(x0 * W), round(y0 * H), round(x1 * W), round(y1 * H)))


def centre_crop_aspect(img, ratio):
    W, H = img.size
    if abs(W / H - ratio) < 1e-3:
        return img
    if W / H > ratio:  # too wide
        nw = round(H * ratio)
        x0 = (W - nw) // 2
        return img.crop((x0, 0, x0 + nw, H))
    nh = round(W / ratio)
    y0 = (H - nh) // 2
    return img.crop((0, y0, W, y0 + nh))


def strip_notes(obj):
    if isinstance(obj, dict):
        return {k: strip_notes(v) for k, v in obj.items() if not k.startswith("_")}
    if isinstance(obj, list):
        return [strip_notes(v) for v in obj]
    return obj


def build(entry):
    src = os.path.join(SRC_DIR, entry["src"])
    out = entry["out"]
    img = ImageOps.exif_transpose(Image.open(src)).convert("RGB")
    src_size = img.size

    if entry.get("crop"):
        img = crop_fraction(img, entry["crop"])
    ratio = parse_aspect(entry["aspect"]) if entry.get("aspect") else None
    if ratio:
        img = centre_crop_aspect(img, ratio)

    width = int(entry["width"])
    warn = ""
    if width > img.width:
        warn = f"source only {img.width}px wide, not upscaled"
        width = img.width
    # With an aspect, derive the height from it so rounding in the crop
    # cannot leave a 1 px error (900x1199 instead of 900x1200).
    height = round(width / ratio) if ratio else round(img.height * width / img.width)
    if (width, height) != img.size:
        img = img.resize((width, height), Image.LANCZOS)

    fix = entry.get("fix") or {}
    if fix:
        rgb = np.asarray(img, dtype=np.float32)
        if fix.get("wb"):
            rgb = white_balance(rgb)
        if fix.get("exposure"):
            rgb = exposure(rgb, float(fix["exposure"]))
        if fix.get("shadow"):
            rgb = shadow_gamma(rgb, float(fix["shadow"]))
        if fix.get("warm"):
            rgb = warm(rgb, float(fix["warm"]))
        img = Image.fromarray(np.clip(rgb + 0.5, 0, 255).astype(np.uint8))

    if entry.get("sharpen", True):
        img = img.filter(ImageFilter.UnsharpMask(
            radius=USM_RADIUS, percent=USM_PERCENT, threshold=USM_THRESHOLD))

    jpg = os.path.join(OUT_DIR, out + ".jpg")
    webp = os.path.join(OUT_DIR, out + ".webp")
    img.save(jpg, "JPEG", quality=JPEG_QUALITY, optimize=True, progressive=True)
    img.save(webp, "WEBP", quality=WEBP_QUALITY, method=6)
    return {
        "out": out, "src": src_size, "size": img.size,
        "jpg_kb": os.path.getsize(jpg) / 1024, "webp_kb": os.path.getsize(webp) / 1024,
        "warn": warn,
    }


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("only", nargs="*", help="build only these 'out' names")
    ap.add_argument("--manifest", default=DEFAULT_MANIFEST)
    args = ap.parse_args()

    with open(args.manifest, encoding="utf-8") as f:
        manifest = strip_notes(json.load(f))
    entries = manifest.get("entries", [])
    if args.only:
        entries = [e for e in entries if e["out"] in args.only]
        missing = set(args.only) - {e["out"] for e in entries}
        if missing:
            sys.exit(f"not in manifest: {', '.join(sorted(missing))}")
    names = [e["out"] for e in entries]
    dupes = {n for n in names if names.count(n) > 1}
    if dupes:
        sys.exit(f"duplicate 'out' names: {', '.join(sorted(dupes))}")
    if not entries:
        print("manifest has no entries; nothing to build")
        return

    os.makedirs(OUT_DIR, exist_ok=True)
    rows, failed = [], 0
    for e in entries:
        try:
            rows.append(build(e))
        except Exception as exc:  # report and continue with the others
            failed += 1
            print(f"FAILED {e.get('out')}: {exc}", file=sys.stderr)

    print(f"{'out':<32} {'source':>11} {'output':>11} {'jpg kB':>8} {'webp kB':>8}")
    for r in rows:
        s = f"{r['src'][0]}x{r['src'][1]}"
        o = f"{r['size'][0]}x{r['size'][1]}"
        print(f"{r['out']:<32} {s:>11} {o:>11} {r['jpg_kb']:>8.0f} {r['webp_kb']:>8.0f}"
              + (f"  ! {r['warn']}" if r["warn"] else ""))
    print(f"{len(rows)} built, {failed} failed -> {os.path.relpath(OUT_DIR, ROOT)}")
    if failed:
        sys.exit(1)


if __name__ == "__main__":
    main()
