---
layout: doc
title: Inputs & Controls
permalink: /docs/components/inputs/
---

# Inputs & Controls

Inputs enable users to enter information and make selections.

## Text Fields

Text fields let users enter text into a UI.

### Filled Text Field
Filled text fields have more visual emphasis than outlined text fields, making them stand out when surrounded by other content and components.

```html
<div class="text-field">
  <input type="text" placeholder="Label">
</div>
```
<div class="text-field">
  <input type="text" placeholder="Label">
</div>

### Outlined Text Field
Outlined text fields have less visual emphasis than filled text fields.

```html
<div class="text-field outlined">
  <input type="text" placeholder="Label">
</div>
```
<div class="text-field outlined">
  <input type="text" placeholder="Label">
</div>

## Selection Controls

### Checkbox
Checkboxes let users select one or more items from a list, or turn an option on or off.

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

### Radio Button
Radio buttons let users select one option from a set.

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

### Switch
Switches toggle the state of a single setting on or off.

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

## Sliders

Sliders allow users to make selections from a range of values.

```html
<div class="slider">
  <input type="range" min="0" max="100" value="50">
</div>
```
<div class="slider">
  <input type="range" min="0" max="100" value="50">
</div>
