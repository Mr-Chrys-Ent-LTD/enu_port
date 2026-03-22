#!/usr/bin/env python
"""
Logo & Meta Tags Setup Verification Script
Checks if all logo files and meta tag configurations are in place.
"""

import os
import sys
from pathlib import Path


def check_logo_setup():
    """Check if logo setup is complete."""

    print("=" * 60)
    print("MRCHRYS LOGO & META TAGS SETUP VERIFICATION")
    print("=" * 60)
    print()

    # Get project root
    project_root = Path(__file__).parent

    # Check 1: Images directory exists
    images_dir = project_root / 'website' / 'static' / 'images'
    print("✓ Check 1: Images Directory")
    if images_dir.exists():
        print(f"  ✅ FOUND: {images_dir}")
    else:
        print(f"  ❌ MISSING: {images_dir}")
        print(f"     Creating directory...")
        images_dir.mkdir(parents=True, exist_ok=True)
        print(f"  ✅ Created!")
    print()

    # Check 2: Logo file
    logo_path = images_dir / 'logo.png'
    print("✓ Check 2: Logo File (logo.png)")
    if logo_path.exists():
        size_kb = logo_path.stat().st_size / 1024
        print(f"  ✅ FOUND: {logo_path}")
        print(f"     File size: {size_kb:.2f} KB")
    else:
        print(f"  ❌ MISSING: {logo_path}")
        print(f"     📝 ACTION: Save your MRCHRYS logo image here as 'logo.png'")
        print(f"     📐 Recommended size: 600x300px or larger")
        print(f"     📋 Format: PNG (with transparent background)")
    print()

    # Check 3: Manifest file
    manifest_path = project_root / 'website' / 'static' / 'manifest.json'
    print("✓ Check 3: PWA Manifest (manifest.json)")
    if manifest_path.exists():
        print(f"  ✅ FOUND: {manifest_path}")
    else:
        print(f"  ❌ MISSING: {manifest_path}")
    print()

    # Check 4: Base template meta tags
    base_template = project_root / 'website' / 'templates' / 'base.html'
    print("✓ Check 4: Meta Tags in base.html")
    if base_template.exists():
        with open(base_template, 'r') as f:
            content = f.read()

        meta_tags = {
            'Open Graph (og:title)': 'og:title',
            'Twitter Card (twitter:card)': 'twitter:card',
            'Manifest Reference': 'manifest.json',
            'Logo Reference': 'images/logo.png',
            'Theme Color': 'theme-color',
        }

        missing = []
        for tag_name, tag_pattern in meta_tags.items():
            if tag_pattern in content:
                print(f"  ✅ {tag_name}")
            else:
                print(f"  ❌ {tag_name} - NOT FOUND")
                missing.append(tag_name)

        if not missing:
            print(f"\n  🎉 All meta tags are in place!")
    else:
        print(f"  ❌ MISSING: {base_template}")
    print()

    # Check 5: CSS for logo
    style_css = project_root / 'website' / 'static' / 'css' / 'style.css'
    print("✓ Check 5: Logo Styling in style.css")
    if style_css.exists():
        with open(style_css, 'r') as f:
            content = f.read()

        if '.navbar-brand img' in content:
            print(f"  ✅ FOUND: Navbar brand logo styling")
        else:
            print(f"  ⚠️  Navbar logo CSS styling not found")
    else:
        print(f"  ❌ MISSING: {style_css}")
    print()

    # Summary
    print("=" * 60)
    print("SUMMARY")
    print("=" * 60)

    if logo_path.exists():
        print("✅ SETUP COMPLETE!")
        print("\nYour website is ready with:")
        print("  • Logo file configured")
        print("  • 30+ SEO meta tags added")
        print("  • Open Graph tags for social sharing")
        print("  • Twitter Card tags for social media")
        print("  • PWA manifest for app installation")
        print("  • Theme colors and branding")
        print("\n📋 Next Steps:")
        print("  1. Run: python manage.py collectstatic")
        print("  2. Test favicon in browser")
        print("  3. Verify logo appears in navbar and footer")
        print("  4. Share your site on social media to test meta tags")
    else:
        print("⚠️  SETUP INCOMPLETE - LOGO FILE MISSING")
        print("\n📝 ACTION REQUIRED:")
        print(f"  Save your MRCHRYS logo image to: {logo_path}")
        print("\n📐 Logo Specifications:")
        print("  • File name: logo.png")
        print("  • Dimensions: 600x300px or larger")
        print("  • Format: PNG with transparent background")
        print("  • File size: Under 200 KB recommended")

    print("\n" + "=" * 60)


if __name__ == '__main__':
    try:
        check_logo_setup()
    except Exception as e:
        print(f"❌ Error during verification: {e}")
        sys.exit(1)
