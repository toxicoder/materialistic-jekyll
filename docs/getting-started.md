---
layout: doc
title: Getting Started
permalink: /getting-started/
---

# Getting Started

## Installation

1. Add the theme to your `Gemfile`:

   ```ruby
   gem "material-tech-theme"
   ```

2. Add the theme to your `_config.yml`:

   ```yaml
   theme: material-tech-theme
   ```

3. Run `bundle install`.

## Usage

Create your markdown files and specify the layout in the front matter.

```yaml
---
layout: doc
title: My Documentation
---
```

## Running Locally

```bash
bundle exec jekyll serve
```
