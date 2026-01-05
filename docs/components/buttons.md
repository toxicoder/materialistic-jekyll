---
layout: doc
title: Buttons
permalink: /docs/components/buttons/
---

# Buttons

Buttons allow users to take actions, and make choices, with a single tap.

## Common Buttons

### Filled Button (Primary)
The filled button is the primary button for the most important action.

```html
<button class="btn btn-primary">Primary</button>
```
<button class="btn btn-primary">Primary</button>

### Outlined Button
Outlined buttons are medium-emphasis buttons. They contain actions that are important but aren't the primary action in an app.

```html
<button class="btn btn-outlined">Outlined</button>
```
<button class="btn btn-outlined">Outlined</button>

### Tonal Button
Tonal buttons are an alternative middle ground between filled and outlined buttons. They're useful in contexts where a lower-priority button requires slightly more emphasis than an outline would give.

```html
<button class="btn btn-tonal">Tonal</button>
```
<button class="btn btn-tonal">Tonal</button>

### Elevated Button
Elevated buttons are essentially filled tonal buttons with a shadow. They prevent separation issues on surfaces that have the same color as the button.

```html
<button class="btn btn-elevated">Elevated</button>
```
<button class="btn btn-elevated">Elevated</button>

### Text Button
Text buttons are used for low-emphasis actions.

```html
<button class="btn btn-text">Text Button</button>
```
<button class="btn btn-text">Text Button</button>

## Floating Action Buttons (FAB)

FABs represent the primary action of a screen.

### Standard FAB
```html
<button class="fab">+</button>
```
<button class="fab" style="font-size:24px;line-height:1">+</button>

### Small FAB
```html
<button class="fab fab-small">+</button>
```
<button class="fab fab-small" style="font-size:20px;line-height:1">+</button>

### Large FAB
```html
<button class="fab fab-large">+</button>
```
<button class="fab fab-large" style="font-size:36px;line-height:1">+</button>

### Extended FAB
Extended FABs are wider and include a text label.

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

## Icon Buttons

Icon buttons help people take minor actions with one tap.

```html
<!-- Standard -->
<button class="icon-btn">★</button>

<!-- Filled -->
<button class="icon-btn filled">★</button>

<!-- Tonal -->
<button class="icon-btn tonal">★</button>

<!-- Outlined -->
<button class="icon-btn outlined">★</button>
```

<div style="display:flex; gap:8px;">
<button class="icon-btn">★</button>
<button class="icon-btn filled">★</button>
<button class="icon-btn tonal">★</button>
<button class="icon-btn outlined">★</button>
</div>

## Segmented Buttons

Segmented buttons help people select options, switch views, or sort elements.

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
