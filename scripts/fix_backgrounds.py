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

def fix_backgrounds():
    with open(INPUT_FILE, 'r') as f:
        content = f.read()

    # Regex to find palette blocks
    palette_pattern = re.compile(r'(\.palette-\d+)\s*{([^}]*)}')

    def replace_block(match):
        header = match.group(1)
        body = match.group(2)

        # Parse variables
        variables = {}
        # The body might contain newlines and spaces, so we split by ;
        statements = body.strip().split(';')

        parsed_vars = {}
        keys_order = []

        for stmt in statements:
            if ':' in stmt:
                parts = stmt.split(':', 1)
                key = parts[0].strip()
                val = parts[1].strip()
                parsed_vars[key] = val
                keys_order.append(key)

        if '--md-sys-color-primary' not in parsed_vars:
            return match.group(0)

        primary_hex = parsed_vars['--md-sys-color-primary']

        # Calculate HLS from primary
        r, g, b = hex_to_rgb(primary_hex)
        h, l, s = colorsys.rgb_to_hls(r, g, b)

        # Define new colors
        # Background: Very light tint (L=98%, S=10%)
        bg_color = rgb_to_hex(colorsys.hls_to_rgb(h, 0.98, 0.10))

        # On-Background (Dark Mode Background): Dark tint (L=8%, S=15%)
        on_bg_color = rgb_to_hex(colorsys.hls_to_rgb(h, 0.08, 0.15))

        # Surface: Match background
        surface_color = bg_color
        on_surface_color = on_bg_color

        # Surface Variant: Slightly darker than background (for light mode) (L=92%)
        surface_variant_color = rgb_to_hex(colorsys.hls_to_rgb(h, 0.92, 0.10))

        # On Surface Variant (Dark Mode Surface Variant): Darker tint but lighter than bg (L=25%)
        on_surface_variant_color = rgb_to_hex(colorsys.hls_to_rgb(h, 0.25, 0.10))

        # Update variables
        parsed_vars['--md-sys-color-background'] = bg_color
        parsed_vars['--md-sys-color-on-background'] = on_bg_color
        parsed_vars['--md-sys-color-surface'] = surface_color
        parsed_vars['--md-sys-color-on-surface'] = on_surface_color
        parsed_vars['--md-sys-color-surface-variant'] = surface_variant_color
        parsed_vars['--md-sys-color-on-surface-variant'] = on_surface_variant_color

        # Reconstruct body preserving order
        new_body = "\n"
        seen_keys = set()
        for key in keys_order:
            new_body += f"  {key}: {parsed_vars[key]};\n"
            seen_keys.add(key)

        return f"{header} {{{new_body}}}"

    new_content = palette_pattern.sub(replace_block, content)

    with open(OUTPUT_FILE, 'w') as f:
        f.write(new_content)

    print(f"Updated {OUTPUT_FILE}")

if __name__ == "__main__":
    fix_backgrounds()
