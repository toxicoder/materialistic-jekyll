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

There are three ways to use this theme:

### 1. As a Ruby Gem (Recommended)

Add this line to your Jekyll site's `Gemfile`:

```ruby
gem "materialistic-jekyll-theme"
```

And add this line to your Jekyll site's `_config.yml`:

```yaml
theme: materialistic-jekyll-theme
```

Then execute:

```bash
$ bundle
```

### 2. As a Remote Theme (GitHub Pages)

If you are hosting on GitHub Pages, you can use the `jekyll-remote-theme` plugin.

Add this to your `Gemfile`:

```ruby
gem "jekyll-remote-theme"
```

And add this to your `_config.yml`:

```yaml
plugins:
  - jekyll-remote-theme

remote_theme: toxicoder/materialistic-jekyll
```

### 3. Forking (Development)

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

You **must** create a `_data/navigation.yml` file to define your sidebar structure.

Example `_data/navigation.yml`:

```yaml
docs:
  - title: Home
    url: /docs/
  - title: Configuration
    children:
      - title: Project Information
        url: /docs/configuration/project-information/
```

If you do not provide this file, the sidebar will attempt to list all pages, which may not be ideal.

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

## Support My Projects

If you find this repository helpful and would like to support its development, consider making a donation:

### GitHub Sponsors
[![Sponsor](https://img.shields.io/badge/Sponsor-%23EA4AAA?style=for-the-badge&logo=github)](https://github.com/sponsors/toxicoder)

### Buy Me a Coffee
<a href="https://www.buymeacoffee.com/toxicoder" target="_blank">
    <img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" height="41" width="174">
</a>

### PayPal
[![PayPal](https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif)](https://www.paypal.com/donate/?hosted_button_id=LSHNL8YLSU3W6)

### Ko-fi
<a href="https://ko-fi.com/toxicoder" target="_blank">
    <img src="https://storage.ko-fi.com/cdn/kofi3.png" alt="Ko-fi" height="41" width="174">
</a>

### Coinbase
[![Donate via Coinbase](https://img.shields.io/badge/Donate%20via-Coinbase-0052FF?style=for-the-badge&logo=coinbase&logoColor=white)](https://commerce.coinbase.com/checkout/e07dc140-d9f7-4818-b999-fdb4f894bab7)

Your support helps maintain and improve this collection of development tools and templates. Thank you for contributing to open source!

## License

[MIT](https://choosealicense.com/licenses/mit/)
