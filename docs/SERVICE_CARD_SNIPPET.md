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

- Use Wikimedia Commons or properly licensed stock images
- Recommended resolution: 640px width minimum
- Images should be relevant to the service
- The semi-transparent overlay ensures text remains readable even with busy backgrounds

## Example with Different Services

### Massage Service
```html
<div
  class="service-card"
  style="background-image: url('https://upload.wikimedia.org/wikipedia/commons/thumb/3/3e/Massage_in_a_spa.jpg/640px-Massage_in_a_spa.jpg')"
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
