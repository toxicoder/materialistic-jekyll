# Materialistic Jekyll Theme

A Jekyll theme for technical documentation built with the latest Google Material Design 3 specifications.

[View Demo](https://toxicoder.github.io/materialistic-jekyll/)

## Features

- **Material Design 3**: Fully compliant with Material You design specs.
- **50 Premade Color Palettes**: Easily switch between 50 diverse color schemes.
- **Developer Optimized**: Typography, code highlighting, and layout optimized for technical docs.
- **Responsive**: Works on mobile, tablet, and desktop.

## Installation

Add this line to your Jekyll site's `Gemfile`:

```ruby
gem "material-tech-theme"
```

And add this line to your Jekyll site's `_config.yml`:

```yaml
theme: material-tech-theme
```

(Note: Since this is a local theme for now, copy the files to your Jekyll project or set it up as a remote theme).

## Usage

### Changing Color Palettes

You can change the color palette by modifying `_config.yml`. The theme supports 50 palettes (`palette-1` to `palette-50`).

```yaml
theme_settings:
  palette: "palette-12"
```

Alternatively, you can override it per page in the Front Matter:

```yaml
---
layout: doc
title: My Page
palette: "palette-4"
---
```

### Layouts

- `default`: Base layout.
- `home`: Landing page layout.
- `doc`: Documentation layout with sidebar navigation.
- `post`: Blog post layout.
- `page`: Standard page layout.

### Documentation Structure

To add pages to the sidebar, create markdown files in your root directory (or subdirectories) and ensure they have a `title` in the Front Matter.

```yaml
---
layout: doc
title: Getting Started
permalink: /getting-started/
---
```

## Customization

To customize the colors further, you can edit `_sass/_palettes.scss` or override the CSS variables in your own CSS file.

## License

MIT
