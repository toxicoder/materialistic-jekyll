# Materialistic Jekyll Theme

A Material Design 3 Jekyll theme for technical documentation. Inspired by the structure of MkDocs, but built natively for Jekyll.

## Features

*   **Material Design 3**: Fully compliant with the latest Material Design specifications (Material You).
*   **Structured Documentation**: Use the `docs/` directory for your content.
*   **Nested Navigation**: Define a hierarchical sidebar in `_data/navigation.yml`.
*   **Search**: Built-in client-side search.
*   **Color Palettes**: 50 pre-made color palettes.
*   **Responsive**: Optimized for mobile, tablet, and desktop.

## Installation

1.  Fork or copy this repository.
2.  Install dependencies:
    ```bash
    bundle install
    ```
3.  Run the server:
    ```bash
    bundle exec jekyll serve
    ```

## Configuration

### Directory Structure

Place your documentation files in the `docs/` directory. You can create subdirectories for better organization.

```
docs/
├── index.md
├── configuration/
│   ├── index.md
│   └── project-information.md
└── advanced/
    └── settings.md
```

### Navigation

Define your sidebar structure in `_data/navigation.yml`.

```yaml
docs:
  - title: Home
    url: /docs/
  - title: Configuration
    children:
      - title: Project Information
        url: /docs/configuration/project-information/
```

### Search

Search is enabled by default. It indexes all pages with a title.

### Customization

You can add extra CSS or JavaScript files by updating `_config.yml`:

```yaml
extra_css:
  - /assets/css/custom.css
extra_javascript:
  - /assets/js/custom.js
```

### Palettes

Change the color palette in `_config.yml`:

```yaml
theme_settings:
  palette: "palette-1" # Options: palette-1 to palette-50
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)
