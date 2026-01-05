---
layout: doc
title: Layout & Navigation
permalink: /docs/components/layout/
---

# Layout & Navigation

Components that help structure the page and navigate between different sections.

## Tabs

Tabs organize content across different screens, data sets, and other interactions.

```html
<div class="tabs">
  <div class="tab-item active">Tab 1</div>
  <div class="tab-item">Tab 2</div>
  <div class="tab-item">Tab 3</div>
</div>
```
<div class="tabs">
  <div class="tab-item active">Tab 1</div>
  <div class="tab-item">Tab 2</div>
  <div class="tab-item">Tab 3</div>
</div>

## Navigation Rail

The navigation rail provides ergonomic movement between primary destinations in apps.

```html
<div class="nav-rail" style="height: 300px; display:inline-flex;">
  <div class="nav-rail-item active">
    <span class="icon">●</span>
    <span class="label">One</span>
  </div>
  <div class="nav-rail-item">
    <span class="icon">○</span>
    <span class="label">Two</span>
  </div>
</div>
```
<div class="nav-rail" style="height: 300px; display:inline-flex;">
  <div class="nav-rail-item active">
    <span class="icon">●</span>
    <span class="label">One</span>
  </div>
  <div class="nav-rail-item">
    <span class="icon">○</span>
    <span class="label">Two</span>
  </div>
</div>

## Bottom Sheets

Bottom sheets display supplementary content and actions on mobile devices.

```html
<div class="bottom-sheet" style="position:relative; transform:none; left:auto; bottom:auto;">
  <div class="drag-handle"></div>
  <div class="sheet-content">
    <p>Bottom sheet content goes here.</p>
  </div>
</div>
```
<div class="bottom-sheet" style="position:relative; transform:none; left:auto; bottom:auto;">
  <div class="drag-handle"></div>
  <div class="sheet-content">
    <p>Bottom sheet content goes here.</p>
  </div>
</div>

## Dialogs

Dialogs provide important prompts in a user flow.

```html
<div class="dialog" style="position: static; transform: none; box-shadow: var(--md-sys-elevation-level-3); margin: 0 auto;">
  <div class="dialog-headline">Dialog Title</div>
  <div class="dialog-content">
    This is a basic dialog example showing the structure.
  </div>
  <div class="dialog-actions">
    <button class="btn btn-text">Cancel</button>
    <button class="btn btn-text">OK</button>
  </div>
</div>
```
<div class="dialog" style="position: static; transform: none; box-shadow: var(--md-sys-elevation-level-3); margin: 0 auto;">
  <div class="dialog-headline">Dialog Title</div>
  <div class="dialog-content">
    This is a basic dialog example showing the structure.
  </div>
  <div class="dialog-actions">
    <button class="btn btn-text">Cancel</button>
    <button class="btn btn-text">OK</button>
  </div>
</div>

## Menus

Menus display a list of choices on a temporary surface.

```html
<div class="menu">
  <div class="menu-item">Item 1</div>
  <div class="menu-item">Item 2</div>
  <div class="menu-item">Item 3</div>
</div>
```
<div class="menu">
  <div class="menu-item">Item 1</div>
  <div class="menu-item">Item 2</div>
  <div class="menu-item">Item 3</div>
</div>

## Dividers

Dividers distinguish between sections of content.

```html
<hr class="divider">
```
<hr class="divider">
