---
layout: default
title: Material 3 Components
permalink: /docs/components/
---

# Material 3 Components

This page demonstrates the implementation of Material 3 components in this theme.
Most components are implemented as CSS classes that can be applied to HTML elements.

## Buttons

### Extended Types

**Elevated Button**
```html
<button class="btn btn-elevated">Elevated</button>
```
<button class="btn btn-elevated">Elevated</button>

**Tonal Button**
```html
<button class="btn btn-tonal">Tonal</button>
```
<button class="btn btn-tonal">Tonal</button>

**Text Button**
```html
<button class="btn btn-text">Text Button</button>
```
<button class="btn btn-text">Text Button</button>

### FAB

**Standard FAB**
```html
<button class="fab">+</button>
```
<button class="fab" style="font-size:24px;line-height:1">+</button>

**Small FAB**
```html
<button class="fab fab-small">+</button>
```
<button class="fab fab-small" style="font-size:20px;line-height:1">+</button>

**Large FAB**
```html
<button class="fab fab-large">+</button>
```
<button class="fab fab-large" style="font-size:36px;line-height:1">+</button>

**Extended FAB**
```html
<button class="fab-extended">
  <span>+</span>
  <span>Create</span>
</button>
```
<button class="fab-extended">
  <span style="font-size:24px;line-height:1">+</span>
  <span>Create</span>
</button>

### Icon Buttons

```html
<button class="icon-btn">
  <span>★</span>
</button>
<button class="icon-btn filled">
  <span>★</span>
</button>
<button class="icon-btn tonal">
  <span>★</span>
</button>
<button class="icon-btn outlined">
  <span>★</span>
</button>
```
<div style="display:flex; gap:8px;">
<button class="icon-btn">★</button>
<button class="icon-btn filled">★</button>
<button class="icon-btn tonal">★</button>
<button class="icon-btn outlined">★</button>
</div>

### Segmented Buttons

```html
<div class="segmented-btn-group">
  <button class="segmented-btn selected">Day</button>
  <button class="segmented-btn">Week</button>
  <button class="segmented-btn">Month</button>
</div>
```
<div class="segmented-btn-group">
  <button class="segmented-btn selected">Day</button>
  <button class="segmented-btn">Week</button>
  <button class="segmented-btn">Month</button>
</div>

## Inputs & Controls

### Text Fields

**Filled**
```html
<div class="text-field">
  <input type="text" placeholder="Label">
</div>
```
<div class="text-field">
  <input type="text" placeholder="Label">
</div>

**Outlined**
```html
<div class="text-field outlined">
  <input type="text" placeholder="Label">
</div>
```
<div class="text-field outlined">
  <input type="text" placeholder="Label">
</div>

### Selection Controls

**Checkbox**
```html
<label class="checkbox-wrapper">
  <input type="checkbox" checked>
  <span>Checked</span>
</label>
<label class="checkbox-wrapper">
  <input type="checkbox">
  <span>Unchecked</span>
</label>
```
<label class="checkbox-wrapper">
  <input type="checkbox" checked>
  <span>Checked</span>
</label>
<label class="checkbox-wrapper">
  <input type="checkbox">
  <span>Unchecked</span>
</label>

**Radio**
```html
<label class="radio-wrapper">
  <input type="radio" name="demo-radio" checked>
  <span>Option 1</span>
</label>
<label class="radio-wrapper">
  <input type="radio" name="demo-radio">
  <span>Option 2</span>
</label>
```
<label class="radio-wrapper">
  <input type="radio" name="demo-radio" checked>
  <span>Option 1</span>
</label>
<label class="radio-wrapper">
  <input type="radio" name="demo-radio">
  <span>Option 2</span>
</label>

**Switch**
```html
<label class="switch">
  <input type="checkbox" checked>
  <span class="slider-track"></span>
</label>
<label class="switch">
  <input type="checkbox">
  <span class="slider-track"></span>
</label>
```
<label class="switch">
  <input type="checkbox" checked>
  <span class="slider-track"></span>
</label>
<label class="switch">
  <input type="checkbox">
  <span class="slider-track"></span>
</label>

**Slider**
```html
<div class="slider">
  <input type="range" min="0" max="100" value="50">
</div>
```
<div class="slider">
  <input type="range" min="0" max="100" value="50">
</div>

## Content & Display

### Cards

**Elevated Card**
```markdown
This is an elevated card.
{: .card .card-elevated }
```
<div class="card card-elevated">
  This is an elevated card.
</div>

**Filled Card**
```markdown
This is a filled card.
{: .card .card-filled }
```
<div class="card card-filled">
  This is a filled card.
</div>

**Outlined Card**
```markdown
This is an outlined card.
{: .card .card-outlined }
```
<div class="card card-outlined">
  This is an outlined card.
</div>

### Lists

```html
<ul class="list">
  <li class="list-item">
    <span class="leading-element avatar">A</span>
    <div class="list-item-content">
      <span class="list-item-headline">Headline</span>
      <span class="list-item-supporting-text">Supporting text</span>
    </div>
    <span class="trailing-element">10m</span>
  </li>
  <li class="list-item divider"></li>
  <li class="list-item">
    <span class="leading-element avatar">B</span>
    <div class="list-item-content">
      <span class="list-item-headline">Headline 2</span>
      <span class="list-item-supporting-text">Supporting text 2</span>
    </div>
    <span class="trailing-element">5m</span>
  </li>
</ul>
```
<ul class="list">
  <li class="list-item">
    <span class="leading-element avatar">A</span>
    <div class="list-item-content">
      <span class="list-item-headline">Headline</span>
      <span class="list-item-supporting-text">Supporting text</span>
    </div>
    <span class="trailing-element">10m</span>
  </li>
  <li class="list-item divider"></li>
  <li class="list-item">
    <span class="leading-element avatar">B</span>
    <div class="list-item-content">
      <span class="list-item-headline">Headline 2</span>
      <span class="list-item-supporting-text">Supporting text 2</span>
    </div>
    <span class="trailing-element">5m</span>
  </li>
</ul>

### Chips

```markdown
Assist
{: .chip }

Filter
{: .chip .filled }

Input
{: .chip .elevated }
```
<span class="chip">Assist</span>
<span class="chip filled">Filter</span>
<span class="chip elevated">Input</span>

### Badge

```html
<span class="badge">3</span>
<span class="badge small"></span>
```
<span class="badge">3</span>
<span class="badge small"></span>

### Tooltip

```html
<span class="tooltip" data-tooltip="This is a tooltip">Hover me</span>
```
<span class="tooltip" data-tooltip="This is a tooltip">Hover me</span>

### Progress Indicators

**Linear**
```html
<div class="progress-linear"></div>
```
<div class="progress-linear"></div>

**Circular**
```html
<div class="progress-circular"></div>
```
<div class="progress-circular"></div>

### Dialog

```html
<div class="dialog">
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
<div class="dialog">
  <div class="dialog-headline">Dialog Title</div>
  <div class="dialog-content">
    This is a basic dialog example showing the structure.
  </div>
  <div class="dialog-actions">
    <button class="btn btn-text">Cancel</button>
    <button class="btn btn-text">OK</button>
  </div>
</div>

### Menu

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

## Navigation

### Tabs

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

### Navigation Rail (Demo)

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

### Bottom Sheet (Demo)

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
