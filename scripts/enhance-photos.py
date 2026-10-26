"""Classical photo enhancement, pass 1. Originals are never modified."""
import glob
import os

import cv2
import numpy as np
from PIL import Image, ImageFilter, ImageOps

# ---- Parameters -----------------------------------------------------------
SRC_DIR = "C:/Users/jpdre/Documents/Projects/251106-Raiz-de-Luz/Cocars/Photos"
OUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "pass1")

WB_BRIGHT_FRACTION = 0.02      # brightest fraction of pixels used as neutral reference
WB_GAIN_MIN, WB_GAIN_MAX = 0.8, 1.25

BLACK_PERCENTILE = 0.3
WHITE_PERCENTILE = 99.7

SHADOW_MEAN_THRESHOLD = 110.0  # lift only if mean luminance (0-255) is below this
SHADOW_GAMMA = 0.92

CLAHE_CLIP = 1.5
CLAHE_TILES = (8, 8)
CLAHE_BLEND = 0.70             # weight of CLAHE L; remainder is original L

VIBRANCE_BOOST = 0.12          # +12% saturation at low saturation
VIBRANCE_KNEE = 0.6            # S above this gets progressively less boost

USM_RADIUS = 1.0
USM_PERCENT = 60               # amount 0.6
USM_THRESHOLD = 2

JPEG_QUALITY = 90
COMPARE_HEIGHT = 900
COMPARE_GUTTER = 10
GUTTER_GREY = 128
# ---------------------------------------------------------------------------


def luminance(rgb):
    return 0.299 * rgb[..., 0] + 0.587 * rgb[..., 1] + 0.114 * rgb[..., 2]


def white_balance(rgb):
    lum = luminance(rgb)
    thr = np.quantile(lum, 1.0 - WB_BRIGHT_FRACTION)
    mask = lum >= thr
    means = rgb[mask].mean(axis=0)
    grey = means.mean()
    gains = np.clip(grey / np.maximum(means, 1e-6), WB_GAIN_MIN, WB_GAIN_MAX)
    return np.clip(rgb * gains, 0, 255), gains


def levels(rgb):
    lum = luminance(rgb)
    bp, wp = np.percentile(lum, [BLACK_PERCENTILE, WHITE_PERCENTILE])
    out = np.clip((rgb - bp) / max(wp - bp, 1e-6) * 255.0, 0, 255)
    return out, bp, wp


def shadow_lift(rgb):
    mean_lum = float(luminance(rgb).mean())
    if mean_lum >= SHADOW_MEAN_THRESHOLD:
        return rgb, mean_lum, False
    lum = np.maximum(luminance(rgb), 1e-3)
    new = 255.0 * (lum / 255.0) ** SHADOW_GAMMA
    out = np.clip(rgb * (new / lum)[..., None], 0, 255)
    return out, mean_lum, True


def local_contrast(rgb):
    u8 = np.clip(rgb + 0.5, 0, 255).astype(np.uint8)
    lab = cv2.cvtColor(u8, cv2.COLOR_RGB2LAB)
    L = lab[..., 0]
    clahe = cv2.createCLAHE(clipLimit=CLAHE_CLIP, tileGridSize=CLAHE_TILES)
    Lc = clahe.apply(L)
    lab[..., 0] = np.clip(
        CLAHE_BLEND * Lc.astype(np.float32) + (1 - CLAHE_BLEND) * L.astype(np.float32) + 0.5,
        0, 255).astype(np.uint8)
    return cv2.cvtColor(lab, cv2.COLOR_LAB2RGB).astype(np.float32)


def vibrance(rgb):
    hsv = cv2.cvtColor(np.clip(rgb, 0, 255).astype(np.float32) / 255.0, cv2.COLOR_RGB2HSV)
    S = hsv[..., 1]
    weight = np.clip((1.0 - S) / (1.0 - VIBRANCE_KNEE), 0.0, 1.0)
    hsv[..., 1] = np.clip(S * (1.0 + VIBRANCE_BOOST * weight), 0, 1)
    return cv2.cvtColor(hsv, cv2.COLOR_HSV2RGB) * 255.0


def sharpen(img):
    return img.filter(ImageFilter.UnsharpMask(
        radius=USM_RADIUS, percent=USM_PERCENT, threshold=USM_THRESHOLD))


def resize_h(img, h):
    w = round(img.width * h / img.height)
    return img.resize((w, h), Image.LANCZOS)


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    files = sorted(glob.glob(os.path.join(SRC_DIR, "*.jpg")))
    lines = []
    for i, path in enumerate(files, 1):
        name = os.path.basename(path)
        orig = ImageOps.exif_transpose(Image.open(path)).convert("RGB")
        rgb = np.asarray(orig, dtype=np.float32)

        rgb, gains = white_balance(rgb)
        rgb, bp, wp = levels(rgb)
        rgb, mean_lum, lifted = shadow_lift(rgb)
        rgb = local_contrast(rgb)
        rgb = vibrance(rgb)
        out = Image.fromarray(np.clip(rgb + 0.5, 0, 255).astype(np.uint8))
        out = sharpen(out)

        out_name = name if name.lower().endswith(".jpg") else name + ".jpg"
        out.save(os.path.join(OUT_DIR, out_name), "JPEG", quality=JPEG_QUALITY)

        a, b = resize_h(orig, COMPARE_HEIGHT), resize_h(out, COMPARE_HEIGHT)
        canvas = Image.new("RGB", (a.width + COMPARE_GUTTER + b.width, COMPARE_HEIGHT),
                           (GUTTER_GREY,) * 3)
        canvas.paste(a, (0, 0))
        canvas.paste(b, (a.width + COMPARE_GUTTER, 0))
        canvas.save(os.path.join(OUT_DIR, f"compare_{i}.jpg"), "JPEG", quality=90)

        lines.append(
            f"[{i}] {name}  ({orig.width}x{orig.height})\n"
            f"    WB gains R,G,B: {gains[0]:.3f}, {gains[1]:.3f}, {gains[2]:.3f}\n"
            f"    black point: {bp:.1f}   white point: {wp:.1f}\n"
            f"    mean luminance (after WB+levels): {mean_lum:.1f}\n"
            f"    shadow lift fired: {'yes' if lifted else 'no'}\n")
        print(lines[-1])

    with open(os.path.join(OUT_DIR, "report.txt"), "w", encoding="utf-8") as f:
        f.write("\n".join(lines))


if __name__ == "__main__":
    main()
