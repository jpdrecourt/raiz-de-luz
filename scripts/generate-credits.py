#!/usr/bin/env python3
"""
Generate photo credits HTML from images-config.json and update creditos.html
"""

import json
import re
from pathlib import Path

def load_config():
    """Load configuration from JSON file"""
    config_path = Path(__file__).parent / "images-config.json"
    with open(config_path, "r", encoding="utf-8") as f:
        return json.load(f)

def generate_credits_html():
    """Generate HTML for photo credits"""
    config = load_config()

    html_parts = []
    html_parts.append('<!-- Photo Credits -->')
    html_parts.append('<section class="credits-section">')
    html_parts.append('  <h3>Créditos Fotográficos</h3>')
    html_parts.append('  <p>Agradecemos aos seguintes fotógrafos do Unsplash pelas suas belas imagens:</p>')
    html_parts.append('  <ul class="credits-list">')

    for img in config["images"]:
        photographer = img.get("photographer", "Unknown")
        photographer_url = img.get("photographer_url", "#")
        unsplash_url = img.get("unsplash_url", "#")
        description = img.get("description", img["name"])

        html_parts.append(f'    <li>')
        html_parts.append(f'      <strong>{description}</strong> - ')
        html_parts.append(f'      Foto de <a href="{photographer_url}" target="_blank" rel="noopener">{photographer}</a> ')
        html_parts.append(f'      no <a href="{unsplash_url}" target="_blank" rel="noopener">Unsplash</a>')
        html_parts.append(f'    </li>')

    html_parts.append('  </ul>')
    html_parts.append('  <p class="unsplash-attribution">')
    html_parts.append('    Todas as fotografias são utilizadas sob a ')
    html_parts.append('    <a href="https://unsplash.com/license" target="_blank" rel="noopener">Licença Unsplash</a>.')
    html_parts.append('  </p>')
    html_parts.append('</section>')

    return '\n'.join(html_parts)

def generate_footer_credits():
    """Generate compact footer credits"""
    config = load_config()

    # Get unique photographers
    photographers = {}
    for img in config["images"]:
        photographer = img.get("photographer", "Unknown")
        photographer_url = img.get("photographer_url", "#")
        if photographer not in photographers:
            photographers[photographer] = photographer_url

    html_parts = []
    html_parts.append('<!-- Compact Photo Credits for Footer -->')
    html_parts.append('<p class="photo-credits">')
    html_parts.append('  Fotografias: ')

    credits = []
    for photographer, url in photographers.items():
        credits.append(f'<a href="{url}" target="_blank" rel="noopener">{photographer}</a>')

    html_parts.append(', '.join(credits))
    html_parts.append(' (Unsplash)')
    html_parts.append('</p>')

    return '\n'.join(html_parts)

def generate_json_ld_credits():
    """Generate Schema.org ImageObject credits"""
    config = load_config()

    credits = []
    for img in config["images"]:
        credit = {
            "@type": "ImageObject",
            "name": img.get("description", img["name"]),
            "contentUrl": f"https://raizdeluz.eu/media/images/{img['name']}.jpg",
            "creator": {
                "@type": "Person",
                "name": img.get("photographer", "Unknown"),
                "url": img.get("photographer_url", "")
            },
            "creditText": f"Photo by {img.get('photographer', 'Unknown')} on Unsplash",
            "license": "https://unsplash.com/license",
            "url": img.get("unsplash_url", "")
        }
        credits.append(credit)

    return json.dumps(credits, indent=2, ensure_ascii=False)

def generate_credits_items_only():
    """Generate just the credit items HTML for insertion into creditos.html"""
    config = load_config()

    # Group images by photographer
    photographers = {}
    for img in config["images"]:
        photographer = img.get("photographer", "Unknown")
        if photographer not in photographers:
            photographers[photographer] = {
                "url": img.get("photographer_url", "#"),
                "images": []
            }
        photographers[photographer]["images"].append(img.get("description", img["name"]))

    # Generate credit items
    html_parts = []
    for photographer, data in photographers.items():
        html_parts.append('          <div class="credit-item">')
        html_parts.append(f'            <h3>{photographer}</h3>')

        # List images
        if len(data["images"]) == 1:
            html_parts.append(f'            <p>')
            html_parts.append(f'              <strong>Fotografia:</strong> {data["images"][0]}')
            html_parts.append(f'            </p>')
        else:
            html_parts.append(f'            <p>')
            html_parts.append(f'              <strong>Fotografias:</strong> {", ".join(data["images"])}')
            html_parts.append(f'            </p>')

        # Photographer link
        html_parts.append(f'            <p>')
        html_parts.append(f'              <a')
        html_parts.append(f'                href="{data["url"]}"')
        html_parts.append(f'                target="_blank"')
        html_parts.append(f'                rel="noopener"')
        html_parts.append(f'                >Perfil no Unsplash</a')
        html_parts.append(f'              >')
        html_parts.append(f'            </p>')
        html_parts.append('          </div>')
        html_parts.append('')

    return '\n'.join(html_parts)

def update_credits_page():
    """Update the creditos.html file with new credits"""
    credits_path = Path(__file__).parent.parent / "docs" / "creditos.html"

    if not credits_path.exists():
        print(f"✗ Error: {credits_path} not found!")
        return False

    # Read current HTML
    with open(credits_path, "r", encoding="utf-8") as f:
        html_content = f.read()

    # Generate new credits items
    new_credits = generate_credits_items_only()

    # Find and replace the credits-list div content
    # Pattern: <div class="credits-list"> ... </div> (with the next div being unsplash-attribution)
    pattern = r'(<div class="credits-list">)(.*?)(</div>\s*<div class="unsplash-attribution")'

    replacement = r'\1\n' + new_credits + r'        \3'

    updated_html = re.sub(pattern, replacement, html_content, flags=re.DOTALL)

    if updated_html == html_content:
        print("⚠️  Warning: Could not find credits-list section to update")
        return False

    # Write updated HTML
    with open(credits_path, "w", encoding="utf-8") as f:
        f.write(updated_html)

    return True

def main():
    print("Photo Credits Generator\n")
    print("=" * 70)

    config = load_config()

    print(f"\nFound {len(config['images'])} images in config")
    print(f"Photographers: {len(set(img.get('photographer', 'Unknown') for img in config['images']))}")

    # Update creditos.html
    print("\nUpdating creditos.html...")
    if update_credits_page():
        print("✓ Successfully updated docs/creditos.html")
    else:
        print("✗ Failed to update creditos.html")

    # Also save reference files
    print("\nGenerating reference files...")

    full_credits = generate_credits_html()
    footer_credits = generate_footer_credits()
    jsonld_credits = generate_json_ld_credits()

    output_path = Path(__file__).parent / "credits-output.html"
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("<!-- FULL CREDITS SECTION -->\n")
        f.write(full_credits)
        f.write("\n\n<!-- FOOTER CREDITS -->\n")
        f.write(footer_credits)
        f.write("\n\n<!-- SCHEMA.ORG JSON-LD -->\n")
        f.write("<script type=\"application/ld+json\">\n")
        f.write(jsonld_credits)
        f.write("\n</script>\n")

    print(f"✓ Reference formats saved to: {output_path}")
    print("\n" + "=" * 70)
    print("Done! 🎉")

if __name__ == "__main__":
    main()
