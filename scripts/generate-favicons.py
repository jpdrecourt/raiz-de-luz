#!/usr/bin/env python3
"""
Generate favicons for Raiz de Luz from the logo image.

Creates multiple favicon sizes with a circular gradient background:
- 80% solid cream color center
- 20% fade to transparency at edges

Usage:
    python3 scripts/generate-favicons.py
"""

from PIL import Image, ImageDraw

# Configuration
LOGO_PATH = 'docs/media/raiz-de-luz-logo-gray.svg'
OUTPUT_DIR = 'docs/media/'
BG_COLOR = (249, 245, 240)  # #f9f5f0 cream color

# Favicon sizes to generate
SIZES = {
    'favicon.ico': (32, 0.80),      # (size, logo_scale)
    'apple-touch-icon.png': (180, 0.85),
    'favicon-192.png': (192, 0.85),
    'favicon-512.png': (512, 0.85),
}


def create_circular_gradient(size, solid_percent=0.80):
    """
    Create a circular gradient with solid center and fade at edges.

    Args:
        size: Canvas size in pixels
        solid_percent: Percentage of radius that should be solid (0.0 to 1.0)

    Returns:
        PIL Image with RGBA circular gradient
    """
    gradient = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(gradient)

    center = size // 2
    max_radius = center
    fade_start_radius = int(max_radius * solid_percent)

    # Draw concentric circles from outside to inside
    for radius in range(max_radius, 0, -1):
        if radius > fade_start_radius:
            # Fade zone (outer portion)
            fade_position = (radius - fade_start_radius) / (max_radius - fade_start_radius)
            alpha = int(255 * (1 - fade_position ** 1.2))
        else:
            # Solid zone (inner portion)
            alpha = 255

        # Create color with alpha
        color = BG_COLOR + (alpha,)

        # Draw circle
        bbox = [center - radius, center - radius, center + radius, center + radius]
        draw.ellipse(bbox, fill=color)

    return gradient


def create_favicon(logo, size, logo_scale=0.85):
    """
    Create a favicon with circular gradient background.

    Args:
        logo: PIL Image of the logo (RGBA)
        size: Output size in pixels
        logo_scale: Logo size as percentage of canvas (0.0 to 1.0)

    Returns:
        PIL Image with favicon
    """
    # Create the circular gradient background
    canvas = create_circular_gradient(size)

    # Calculate logo size and resize
    logo_size = int(size * logo_scale)
    logo_resized = logo.resize((logo_size, logo_size), Image.Resampling.LANCZOS)

    # Calculate position to center logo
    paste_pos = ((size - logo_size) // 2, (size - logo_size) // 2)

    # Paste logo onto background
    canvas.paste(logo_resized, paste_pos, logo_resized)

    return canvas


def main():
    """Generate all favicons from the logo."""
    print(f"Loading logo from: {LOGO_PATH}")
    logo = Image.open(LOGO_PATH).convert('RGBA')

    print(f"\nGenerating favicons with circular gradient background:")
    print(f"- Background: Cream #{BG_COLOR[0]:02x}{BG_COLOR[1]:02x}{BG_COLOR[2]:02x}")
    print(f"- Gradient: 80% solid center, 20% fade at edges\n")

    for filename, (size, logo_scale) in SIZES.items():
        output_path = OUTPUT_DIR + filename
        print(f"Creating {filename} ({size}x{size})...")

        # Create favicon
        favicon = create_favicon(logo, size, logo_scale)

        # Save with appropriate format
        if filename.endswith('.ico'):
            favicon.save(output_path, format='ICO')
        else:
            favicon.save(output_path, format='PNG')

        print(f"  → Saved to {output_path}")

    print("\n✓ All favicons generated successfully!")


if __name__ == '__main__':
    main()
