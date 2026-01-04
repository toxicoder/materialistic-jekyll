import re

def generate_dark_mode(input_file, output_file):
    with open(input_file, 'r') as f:
        content = f.read()

    # Regex to find palette blocks
    palette_pattern = re.compile(r'(\.palette-\d+)\s*{([^}]*)}')

    matches = palette_pattern.findall(content)

    dark_mode_css = "// Generated Dark Mode Overrides\n\n"

    # Define swaps (key <-> value)
    # We will look for keys like --md-sys-color-surface and swap its value with --md-sys-color-on-surface
    # But since we have the values in the block, we can just extract them.

    pairs_to_swap = [
        ('surface', 'on-surface'),
        ('background', 'on-background'),
        ('primary-container', 'on-primary-container'),
        ('secondary-container', 'on-secondary-container'),
        ('tertiary-container', 'on-tertiary-container'),
        ('surface-variant', 'on-surface-variant')
    ]

    for palette_name, body in matches:
        dark_mode_css += f".dark{palette_name} {{\n"

        # Parse variables in the body
        variables = {}
        for line in body.split(';'):
            if ':' in line:
                key, value = line.split(':', 1)
                variables[key.strip()] = value.strip()

        # Perform swaps
        for a, b in pairs_to_swap:
            key_a = f"--md-sys-color-{a}"
            key_b = f"--md-sys-color-{b}"

            if key_a in variables and key_b in variables:
                val_a = variables[key_a]
                val_b = variables[key_b]

                dark_mode_css += f"  {key_a}: {val_b};\n"
                dark_mode_css += f"  {key_b}: {val_a};\n"

        dark_mode_css += "}\n\n"

    with open(output_file, 'w') as f:
        f.write(dark_mode_css)

if __name__ == "__main__":
    generate_dark_mode('_sass/_palettes.scss', '_sass/_dark_mode.scss')
