# Raiz de Luz

Website for Raiz de Luz - Shamanic Massage and Wellness clinic.

## Overview

This is a static website built with HTML, CSS, and vanilla JavaScript. It's designed to be simple, maintainable, and easily deployable to platforms like GitHub Pages, Netlify, or Vercel.

## Structure

```
docs/
├── index.html         # Home page
├── servicos.html      # Services page
├── sobre.html         # About page
├── contacto.html      # Contact page
├── css/
│   └── style.css      # Main stylesheet
├── js/
│   ├── main.js        # Main JavaScript utilities
│   └── contact-form.js # Contact form handler
└── media/
    ├── raiz-de-luz-logo.png    # Main logo
    ├── favicon.ico              # Browser favicon (32x32)
    ├── apple-touch-icon.png     # iOS home screen icon (180x180)
    ├── favicon-192.png          # Android icon (192x192)
    └── favicon-512.png          # Android splash (512x512)

scripts/
└── generate-favicons.py   # Favicon generator script
```

## Features

- **Responsive Design**: Works on all devices from mobile to desktop
- **Portuguese (Portugal) Content**: All content in PT-PT
- **Service Pages**: Detailed information about services offered
- **Contact Form**: Basic client-side validation (needs backend integration)
- **Smooth Animations**: Fade-in effects and smooth scrolling
- **SEO Friendly**: Proper meta tags and semantic HTML

## Getting Started

### Prerequisites

- Node.js (for development tools)
- A text editor (VS Code recommended)
- Git

### Installation

1. Clone the repository
2. Install dependencies:
   ```bash
   npm install
   ```

### Development

The website is in the `docs/` directory. You can:

1. Open `docs/index.html` directly in a browser, or
2. Use a local server:
   ```bash
   # Using Python
   python -m http.server 8000 --directory docs

   # Using Node.js (npx)
   npx serve docs
   ```

3. Run linting:
   ```bash
   npm run lint
   ```

4. Format code:
   ```bash
   npm run prettier
   ```

## Customization

### Content

- **Logo**: Replace `docs/media/raiz-de-luz-logo.png` with your logo
- **Header Image**: Replace `docs/media/header-image.jpg` with your image
- **Service Images**: Add images to `docs/media/` and update references in HTML
- **Text**: Edit the HTML files to update content
- **Contact Info**: Update phone, email, and address in all pages

### Favicons

The website includes favicons for all platforms (browser, iOS, Android). To regenerate them after updating the logo:

```bash
# Prerequisites
pip3 install Pillow

# Generate all favicons from the logo
python3 scripts/generate-favicons.py
```

**What it generates:**
- `favicon.ico` (32×32) - Standard browser favicon
- `apple-touch-icon.png` (180×180) - iOS home screen icon
- `favicon-192.png` (192×192) - Android home screen icon
- `favicon-512.png` (512×512) - Android splash screen

**Design:** Circular gradient background (80% solid cream center, 20% fade to transparency at edges) with centered logo.

**Customization:** Edit `scripts/generate-favicons.py` to adjust:
- Background color (`BG_COLOR`)
- Gradient ratio (solid vs. fade percentage)
- Logo scale (size relative to canvas)
- Output sizes

### Styling

Colors and styling can be customized in `docs/css/style.css`:

```css
:root {
  --primary-color: #6b8e6f; /* Main color */
  --secondary-color: #d4a574; /* Accent color */
  --fg-color: #333; /* Text color */
  --text-light: #666; /* Light text */
  --bg-light: #f9f9f9; /* Background color */
  --border-light: #eee; /* Borders */
}
```

### Contact Form

The contact form currently only has client-side validation. To make it functional, you need to:

1. **Option 1 - Use a Service**:
   - [Formspree](https://formspree.io/)
   - [FormSubmit](https://formsubmit.co/)
   - [Netlify Forms](https://www.netlify.com/products/forms/)

2. **Option 2 - Build Your Own Backend**:
   - Create an API endpoint that receives form data
   - Update `docs/js/contact-form.js` with your endpoint

Example integration code is provided in `contact-form.js`.

## Deployment

### GitHub Pages

1. Push your code to GitHub
2. Go to repository Settings > Pages
3. Set source to the `docs/` folder
4. Your site will be available at `https://yourusername.github.io/repo-name/`

### Netlify

1. Sign up at [Netlify](https://www.netlify.com/)
2. Connect your GitHub repository
3. Set build directory to `docs/`
4. Deploy!

### Vercel

1. Sign up at [Vercel](https://vercel.com/)
2. Import your repository
3. Set output directory to `docs/`
4. Deploy!

## Pages

- **Início (Home)**: Overview and services highlights
- **Serviços (Services)**: Detailed service descriptions
- **Sobre (About)**: About the clinic and therapists
- **Contacto (Contact)**: Contact information and form

## To-Do

- [x] Add actual logo and images
- [x] Create favicons for all platforms
- [ ] Fill in therapist information
- [ ] Add location/address details
- [ ] Integrate contact form with email service
- [ ] Add Google Maps embed
- [ ] Add social media links
- [ ] Consider adding booking/scheduling system
- [ ] Add products page/section if needed
- [ ] Test on all devices
- [ ] Set up analytics (Google Analytics, etc.)

## Browser Support

- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)
- Mobile browsers (iOS Safari, Chrome Mobile)

## License

All rights reserved - Raiz de Luz

## Contact

For questions or support, please contact: info@raizdeluz.pt
