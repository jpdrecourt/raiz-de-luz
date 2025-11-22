# Service Card Snippet

This document provides the HTML pattern for creating service cards with background images.

## Basic Structure

```html
<div
  class="service-card"
  style="background-image: url('IMAGE_URL_HERE')"
>
  <h3>Service Title</h3>
  <p>Service description text goes here.</p>
  <a href="servicos.html#service-anchor" class="card-link">Saiba Mais</a>
</div>
```

## Key Features

1. **Background Image**: Added via inline `style` attribute with `background-image` property
2. **Consistent Layout**: The card uses flexbox to ensure the "Saiba Mais" link is always at the bottom
3. **Semi-transparent Overlay**: A white overlay (92% opacity) ensures text readability over any background image
4. **Hover Effects**:
   - Card lifts up slightly (`translateY(-4px)`)
   - Overlay becomes slightly more transparent (88% opacity) to show more of the background image
   - Shadow increases for depth

## CSS Classes

- `.service-card` - Main card container with flexbox layout
- `.card-link` - Styled link for "Saiba Mais" button

## Image Guidelines

### Current Placeholder Images

The service cards currently use **Unsplash** placeholder images. These are:
- **Free to use** without attribution (Unsplash License)
- **High quality** stock photos
- **Temporary** - you should replace them with your own images for better brand consistency

### Recommended Image Sources

1. **Your own photos**: Best for authenticity and brand identity
2. **Unsplash** (https://unsplash.com): Free high-quality images, no attribution required
3. **Pexels** (https://pexels.com): Free stock photos and videos
4. **Pixabay** (https://pixabay.com): Free images and videos
5. **Wikimedia Commons** (https://commons.wikimedia.org): Free licensed media

### Image Specifications

- **Resolution**: Minimum 640px width recommended
- **Format**: JPG or PNG
- **Subject**: Should be relevant to the specific service
- **Composition**: Avoid busy/cluttered images; the overlay helps but simpler is better

### Replacing Images

To replace an image, simply update the URL in the `style` attribute:

```html
<!-- Before -->
<div class="service-card" style="background-image: url('https://images.unsplash.com/photo-1234567890')">

<!-- After -->
<div class="service-card" style="background-image: url('path/to/your/image.jpg')">
```

## Examples

### With Unsplash Image
```html
<div
  class="service-card"
  style="background-image: url('https://images.unsplash.com/photo-1544161515-4ab6ce6db874?w=640&q=80')"
>
  <h3>Massagem terapêutica</h3>
  <p>Alívio de dores musculares e tensões através de técnicas especializadas de massagem profunda.</p>
  <a href="servicos.html#massagem-terapeutica" class="card-link">Saiba Mais</a>
</div>
```

### With Local Image
```html
<div
  class="service-card"
  style="background-image: url('media/services/therapeutic-massage.jpg')"
>
  <h3>Massagem terapêutica</h3>
  <p>Alívio de dores musculares e tensões através de técnicas especializadas de massagem profunda.</p>
  <a href="servicos.html#massagem-terapeutica" class="card-link">Saiba Mais</a>
</div>
```

### Without Background Image
If you want a card without a background image, simply omit the `style` attribute:

```html
<div class="service-card">
  <h3>Service Title</h3>
  <p>Service description.</p>
  <a href="servicos.html#service-anchor" class="card-link">Saiba Mais</a>
</div>
```

The card will display with a plain white background.
