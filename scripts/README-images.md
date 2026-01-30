# Image Download and Conversion Script

This script downloads all background images from Unsplash and converts them to optimized WebP and JPEG formats.

## Prerequisites

Install required Python packages:

```bash
pip install requests Pillow
```

## Configuration

Edit `images-config.json` to customize:
- Output directory
- JPEG/WebP quality settings
- Image URLs and names

## Usage

### Basic Usage (skip existing images)

```bash
cd scripts
python download-and-convert-images.py
```

### List Image Status

Check which images exist without downloading:

```bash
python download-and-convert-images.py --list
```

### Force Re-download

Re-download all images even if they exist:

```bash
python download-and-convert-images.py --force
```

### Help

```bash
python download-and-convert-images.py --help
```

## What It Does

1. **Downloads** 8 background images from Unsplash at 1920px width
2. **Converts** each image to:
   - **JPEG** format (quality 70%, optimized, progressive)
   - **WebP** format (quality 75%, maximum compression)
3. **Saves** all images to `docs/media/images/`

## Output

The script will create 16 files (8 services × 2 formats):

- `massage-therapeutic.jpg` / `.webp`
- `massage-sports.jpg` / `.webp`
- `massage-prenatal.jpg` / `.webp`
- `therapy-craniosacral.jpg` / `.webp`
- `lymphatic-drainage.jpg` / `.webp`
- `relaxation.jpg` / `.webp`
- `shamanic-massage.jpg` / `.webp`
- `natural-products.jpg` / `.webp`

## Expected Results

- **JPEG files**: ~100-200 KB each
- **WebP files**: ~60-120 KB each (40-50% smaller)
- **Total size**: ~1-2 MB for all images

## Benefits

✓ **40-50% smaller** file sizes with WebP
✓ **Faster page loads** with optimized images
✓ **No external dependencies** on Unsplash CDN
✓ **Better privacy** - no external tracking
✓ **SEO improvement** - local hosting preferred by search engines

## Browser Support

WebP is supported by 96%+ of browsers (all modern browsers). The HTML automatically uses WebP with JPEG fallback for older browsers.

## Photo Credits & Attribution

All photos from Unsplash should be credited. Use the `generate-credits.py` script to automatically update the credits page:

```bash
python generate-credits.py
```

**What it does:**
- ✅ Automatically updates `docs/creditos.html` with all photographer credits
- ✅ Groups images by photographer
- ✅ Generates reference files in `credits-output.html` for other uses

**Output:**
```
Found 10 images in config
Photographers: 7

Updating creditos.html...
✓ Successfully updated docs/creditos.html
✓ Reference formats saved to: credits-output.html
Done! 🎉
```

The script also generates three reference formats in `credits-output.html`:
1. **Full Credits Section** - Complete HTML section
2. **Compact Footer Credits** - Short version for footers
3. **Schema.org JSON-LD** - Structured data for SEO

## Adding New Images

1. Add image info to `images-config.json`:
   ```json
   {
     "name": "new-service",
     "remote_url": "https://images.unsplash.com/photo-{PHOTO_ID}?w=1920&q=75",
     "description": "New Service background",
     "photographer": "Photographer Name",
     "photographer_url": "https://unsplash.com/@photographer",
     "unsplash_url": "https://unsplash.com/photos/{PHOTO_ID}"
   }
   ```

2. Run download script: `python download-and-convert-images.py`

3. Update credits automatically: `python generate-credits.py`

4. Update HTML to use the new image: `media/images/new-service.webp`

**Note:** The credits page (`creditos.html`) will be automatically updated by the script!
