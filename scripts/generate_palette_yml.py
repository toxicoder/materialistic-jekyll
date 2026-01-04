import re
import colorsys

# Existing names mapping to preserve specific names if desired
known_names = {
    "palette-1": "Purple",
    "palette-25": "Deep Blue",
    "palette-16": "Red",
    "palette-9": "Teal",
    "palette-6": "Gold",
    "palette-30": "Pink"
}

def get_color_name(h, s, v):
    # h is 0..1
    deg = h * 360

    if s < 0.1: return "Gray"
    if v < 0.1: return "Black"

    if deg < 15: return "Red"
    elif deg < 45: return "Orange"
    elif deg < 70: return "Yellow"
    elif deg < 150: return "Green"
    elif deg < 190: return "Cyan"
    elif deg < 260: return "Blue"
    elif deg < 290: return "Purple"
    elif deg < 340: return "Pink"
    else: return "Red"

def hex_to_rgb(hex_str):
    hex_str = hex_str.lstrip('#')
    return tuple(int(hex_str[i:i+2], 16)/255.0 for i in (0, 2, 4))

palettes = []
with open('_sass/_palettes.scss', 'r') as f:
    content = f.read()

    blocks = re.split(r'\.palette-', content)[1:] # skip prelude

    for block in blocks:
        # The first chars are the ID until '{' or whitespace
        pid_match = re.match(r'^(\d+)', block)
        if not pid_match: continue
        pid = pid_match.group(1)
        palette_id = f"palette-{pid}"

        # find primary color
        primary_match = re.search(r'--md-sys-color-primary:\s*(#[0-9A-Fa-f]{6})', block)
        if primary_match:
            hex_col = primary_match.group(1)
            r, g, b = hex_to_rgb(hex_col)
            h, s, v = colorsys.rgb_to_hsv(r, g, b)

            base_name = known_names.get(palette_id)
            if not base_name:
                color_name = get_color_name(h, s, v)
                base_name = f"{color_name} {pid}"

            palettes.append({
                "id": palette_id,
                "name": base_name,
                "color": hex_col,
                "pid": int(pid)
            })

palettes.sort(key=lambda x: x['pid'])

with open('_data/palettes.yml', 'w') as f:
    for p in palettes:
        f.write(f"- id: {p['id']}\n")
        f.write(f"  name: \"{p['name']}\"\n")
        f.write(f"  color: \"{p['color']}\"\n")

print(f"Generated _data/palettes.yml with {len(palettes)} palettes.")
