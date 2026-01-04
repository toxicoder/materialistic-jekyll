import re
import colorsys

INPUT_FILE = '_sass/_palettes.scss'
OUTPUT_FILE = '_sass/_palettes.scss'

def hex_to_rgb(hex_str):
    hex_str = hex_str.lstrip('#')
    return tuple(int(hex_str[i:i+2], 16)/255.0 for i in (0, 2, 4))

def rgb_to_hex(rgb):
    return '#{:02x}{:02x}{:02x}'.format(
        max(0, min(255, int(rgb[0]*255 + 0.5))),
        max(0, min(255, int(rgb[1]*255 + 0.5))),
        max(0, min(255, int(rgb[2]*255 + 0.5)))
    ).upper()

def process_color(key, hex_color):
    if not hex_color.startswith('#') or len(hex_color) != 7:
        return hex_color

    r, g, b = hex_to_rgb(hex_color)
    h, l, s = colorsys.rgb_to_hls(r, g, b)

    # Don't touch black/white/grays if they are very desaturated
    if s < 0.02:
        return hex_color

    new_s = s
    new_l = l

    # Strategy:
    # 1. Main colors (Primary, Secondary, Tertiary): High saturation
    if key in ['primary', 'secondary', 'tertiary']:
        # Boost saturation significantly
        new_s = min(0.9, max(0.6, s * 2.5))

    # 2. Containers: Moderate saturation, High lightness (for light mode)
    elif 'container' in key and 'on-' not in key:
        # Boost saturation but cap it to avoid neon backgrounds
        new_s = min(0.35, max(0.15, s * 2.0))

    # 3. Surface/Background: Low saturation, very high lightness
    elif key in ['surface', 'background', 'surface-variant']:
         # Slight boost to tint
        new_s = min(0.2, s * 1.5)

    # 4. On-colors: Usually dark text
    elif 'on-' in key:
        # Tint dark text slightly more to match the richness
        new_s = min(0.5, s * 1.5)

    r, g, b = colorsys.hls_to_rgb(h, new_l, new_s)
    return rgb_to_hex((r, g, b))


def update_palettes():
    with open(INPUT_FILE, 'r') as f:
        content = f.read()

    def replacer(match):
        key = match.group(1) # e.g. primary
        val = match.group(2) # e.g. #6750A4

        new_val = process_color(key, val)
        return f"--md-sys-color-{key}: {new_val}"

    # Pattern: --md-sys-color-([a-z-]+): (#[\da-fA-F]{6})
    new_content = re.sub(r'--md-sys-color-([a-z-]+): (#[\da-fA-F]{6})', replacer, content)

    with open(OUTPUT_FILE, 'w') as f:
        f.write(new_content)

    print(f"Updated {OUTPUT_FILE}")

if __name__ == "__main__":
    update_palettes()
