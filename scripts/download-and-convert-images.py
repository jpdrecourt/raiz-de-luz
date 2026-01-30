#!/usr/bin/env python3
"""
Download background images from Unsplash and convert to optimized WebP format
"""

import argparse
import json
import requests
from pathlib import Path
from PIL import Image
import io

def load_config():
    """Load configuration from JSON file"""
    config_path = Path(__file__).parent / "images-config.json"
    with open(config_path, "r", encoding="utf-8") as f:
        return json.load(f)

def check_existing_images(output_dir: Path, name: str):
    """Check if JPEG and WebP already exist"""
    jpeg_path = output_dir / f"{name}.jpg"
    webp_path = output_dir / f"{name}.webp"

    jpeg_exists = jpeg_path.exists()
    webp_exists = webp_path.exists()

    if jpeg_exists and webp_exists:
        jpeg_size = jpeg_path.stat().st_size / 1024
        webp_size = webp_path.stat().st_size / 1024
        return True, f"JPEG: {jpeg_size:.1f} KB, WebP: {webp_size:.1f} KB"
    elif jpeg_exists:
        return True, "JPEG exists, WebP missing"
    elif webp_exists:
        return True, "WebP exists, JPEG missing"
    else:
        return False, None

def convert_local_file(
    name: str,
    local_file: str,
    output_dir: Path,
    jpeg_quality: int,
    webp_quality: int,
    force: bool = False
):
    """Convert existing local file to optimized JPEG and WebP"""

    # Check if images already exist
    exists, info = check_existing_images(output_dir, name)
    if exists and not force:
        print(f"⊘ Skipping {name} - already exists ({info})")
        return

    local_path = output_dir / local_file
    if not local_path.exists():
        print(f"✗ Local file not found: {local_file}")
        return

    print(f"⟳ Converting {name} from {local_file}...")

    try:
        # Open existing local image
        img = Image.open(local_path)

        # Convert to RGB if necessary
        if img.mode in ("RGBA", "P", "LA"):
            rgb_img = Image.new("RGB", img.size, (255, 255, 255))
            if img.mode == "P":
                img = img.convert("RGBA")
            rgb_img.paste(img, mask=img.split()[-1] if img.mode in ("RGBA", "LA") else None)
            img = rgb_img
        elif img.mode != "RGB":
            img = img.convert("RGB")

        # Save as optimized JPEG
        jpeg_path = output_dir / f"{name}.jpg"
        img.save(jpeg_path, "JPEG", quality=jpeg_quality, optimize=True, progressive=True)
        jpeg_size = jpeg_path.stat().st_size / 1024
        print(f"  ✓ Saved JPEG: {jpeg_path.name} ({jpeg_size:.1f} KB)")

        # Save as WebP
        webp_path = output_dir / f"{name}.webp"
        img.save(webp_path, "WEBP", quality=webp_quality, method=6)
        webp_size = webp_path.stat().st_size / 1024
        savings = ((jpeg_size - webp_size) / jpeg_size) * 100
        print(f"  ✓ Saved WebP: {webp_path.name} ({webp_size:.1f} KB, {savings:.1f}% smaller)")

    except Exception as e:
        print(f"  ✗ Error converting {name}: {e}")

def download_and_convert(
    name: str,
    url: str,
    output_dir: Path,
    jpeg_quality: int,
    webp_quality: int,
    force: bool = False
):
    """Download image and save as optimized JPEG and WebP"""

    # Check if images already exist
    exists, info = check_existing_images(output_dir, name)
    if exists and not force:
        print(f"⊘ Skipping {name} - already exists ({info})")
        return

    print(f"↓ Downloading {name}...")

    try:
        # Download image
        response = requests.get(url, timeout=30)
        response.raise_for_status()

        # Open image with PIL
        img = Image.open(io.BytesIO(response.content))

        # Convert to RGB if necessary (for WebP compatibility)
        if img.mode in ("RGBA", "P", "LA"):
            rgb_img = Image.new("RGB", img.size, (255, 255, 255))
            if img.mode == "P":
                img = img.convert("RGBA")
            rgb_img.paste(img, mask=img.split()[-1] if img.mode in ("RGBA", "LA") else None)
            img = rgb_img
        elif img.mode != "RGB":
            img = img.convert("RGB")

        # Save as optimized JPEG
        jpeg_path = output_dir / f"{name}.jpg"
        img.save(jpeg_path, "JPEG", quality=jpeg_quality, optimize=True, progressive=True)
        jpeg_size = jpeg_path.stat().st_size / 1024
        print(f"  ✓ Saved JPEG: {jpeg_path.name} ({jpeg_size:.1f} KB)")

        # Save as WebP
        webp_path = output_dir / f"{name}.webp"
        img.save(webp_path, "WEBP", quality=webp_quality, method=6)
        webp_size = webp_path.stat().st_size / 1024
        savings = ((jpeg_size - webp_size) / jpeg_size) * 100
        print(f"  ✓ Saved WebP: {webp_path.name} ({webp_size:.1f} KB, {savings:.1f}% smaller)")

    except Exception as e:
        print(f"  ✗ Error downloading {name}: {e}")

def main():
    parser = argparse.ArgumentParser(
        description="Download and convert images from Unsplash"
    )
    parser.add_argument(
        "--force",
        "-f",
        action="store_true",
        help="Force re-download even if images already exist"
    )
    parser.add_argument(
        "--list",
        "-l",
        action="store_true",
        help="List all images and their status without downloading"
    )
    args = parser.parse_args()

    # Load configuration
    config = load_config()
    output_dir = Path(__file__).parent / config["output_dir"]
    output_dir.mkdir(parents=True, exist_ok=True)

    print("Image Download and Conversion Tool")
    print(f"Output directory: {output_dir}")
    print(f"JPEG quality: {config['jpeg_quality']}%")
    print(f"WebP quality: {config['webp_quality']}%")
    print()

    # List mode
    if args.list:
        print("Image Status:")
        print("-" * 70)
        for img_config in config["images"]:
            name = img_config["name"]
            exists, info = check_existing_images(output_dir, name)
            status = f"✓ {info}" if exists else "✗ Missing"
            print(f"{name:30} {status}")
        print()
        return

    # Check if PIL supports WebP
    try:
        img = Image.new("RGB", (1, 1))
        img.save(io.BytesIO(), "WEBP")
        print("✓ WebP support detected\n")
    except Exception:
        print("⚠️  WARNING: PIL doesn't support WebP. Install with: pip install Pillow")
        print("    Falling back to JPEG only.\n")

    # Download mode
    skipped = 0
    downloaded = 0
    errors = 0

    for img_config in config["images"]:
        name = img_config["name"]

        exists, _ = check_existing_images(output_dir, name)
        if exists and not args.force:
            skipped += 1

        # Handle local files vs remote downloads
        if "local_file" in img_config:
            convert_local_file(
                name,
                img_config["local_file"],
                output_dir,
                config["jpeg_quality"],
                config["webp_quality"],
                force=args.force
            )
        elif "remote_url" in img_config:
            download_and_convert(
                name,
                img_config["remote_url"],
                output_dir,
                config["jpeg_quality"],
                config["webp_quality"],
                force=args.force
            )
        else:
            print(f"✗ Error: {name} has no remote_url or local_file")
            errors += 1
            continue

        # Check if download succeeded
        if check_existing_images(output_dir, name)[0]:
            if not exists or args.force:
                downloaded += 1
        else:
            errors += 1

        print()

    # Summary
    print("=" * 70)
    print("Summary:")
    if downloaded > 0:
        print(f"  ✓ Downloaded: {downloaded} images")
    if skipped > 0:
        print(f"  ⊘ Skipped: {skipped} images (already exist)")
    if errors > 0:
        print(f"  ✗ Errors: {errors} images")

    total_images = len(list(output_dir.glob("*.jpg"))) + len(list(output_dir.glob("*.webp")))
    print(f"\nTotal files in directory: {total_images}")

    if skipped > 0 and not args.force:
        print("\nTip: Use --force to re-download existing images")

    print()

if __name__ == "__main__":
    main()
