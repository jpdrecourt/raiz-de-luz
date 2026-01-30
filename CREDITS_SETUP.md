# Photo Credits Setup - Complete Guide

## 📝 Adding New Images in Future

When you add a new service with a new image:

1. **Add to config** (`scripts/images-config.json`):

   ```json
   {
     "name": "new-service",
     "remote_url": "https://images.unsplash.com/photo-...",
     "description": "New Service background",
     "photographer": "Photographer Name",
     "photographer_url": "https://unsplash.com/@username",
     "unsplash_url": "https://unsplash.com/photos/..."
   }
   ```

2. **Download image:**

   ```bash
   python scripts/download-and-convert-images.py
   ```

3. **Update credits page:**

   ```bash
   python scripts/generate-credits.py
   ```

   Then copy the new photographer entry to `creditos.html`

4. **Update HTML:**
   Use `media/images/new-service.webp` in your service section

## ✨ Benefits of This Setup

✅ **Proper Attribution** - Credits all photographers as requested by Unsplash
✅ **Centralized** - One page for all credits, easy to maintain
✅ **SEO Friendly** - Links to photographers help with backlinks
✅ **Professional** - Shows you respect artists' work
✅ **Automated** - Scripts make it easy to add new images
✅ **Legal Compliance** - Follows Unsplash license requirements

## 🔗 Important Links

- Credits Page: https://raizdeluz.eu/creditos.html
- Unsplash License: https://unsplash.com/license
- Image Scripts: `/scripts/` folder
- Config File: `/scripts/images-config.json`
