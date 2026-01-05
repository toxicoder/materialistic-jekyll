---
layout: doc
title: Content & Display
permalink: /docs/components/content/
---

# Content & Display

These components help organize and display content.

## Cards

Cards contain content and actions about a single subject.

### Elevated Card
Elevated cards have a shadow and a background color.

```markdown
This is an elevated card.
{: .card .card-elevated }
```
<div class="card card-elevated">
  This is an elevated card.
</div>

### Filled Card
Filled cards have a background color but no shadow.

```markdown
This is a filled card.
{: .card .card-filled }
```
<div class="card card-filled">
  This is a filled card.
</div>

### Outlined Card
Outlined cards have a border and a transparent background.

```markdown
This is an outlined card.
{: .card .card-outlined }
```
<div class="card card-outlined">
  This is an outlined card.
</div>

## Lists

Lists are continuous, vertical indexes of text or images.

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

## Chips

Chips help people enter information, make selections, filter content, or trigger actions.

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

## Badges

Badges show notifications, counts, or status information on other components.

```html
<span class="badge">3</span>
<span class="badge small"></span>
```
<span class="badge">3</span>
<span class="badge small"></span>

## Tooltips

Tooltips display informative text when users hover over, focus on, or tap an element.

```html
<span class="tooltip" data-tooltip="This is a tooltip">Hover me</span>
```
<span class="tooltip" data-tooltip="This is a tooltip">Hover me</span>

## Progress Indicators

Progress indicators express an unspecified wait time or display the length of a process.

### Linear Progress
```html
<div class="progress-linear"></div>
```
<div class="progress-linear"></div>

### Circular Progress
```html
<div class="progress-circular"></div>
```
<div class="progress-circular"></div>

## Snackbars

Snackbars provide brief messages about app processes at the bottom of the screen.

```html
<div class="snackbar" style="position: static; transform: none; margin: 0 auto;">
  <span class="snackbar-text">Single-line snackbar</span>
  <button class="snackbar-action">Action</button>
</div>
```
<div class="snackbar" style="position: static; transform: none; margin: 0 auto;">
  <span class="snackbar-text">Single-line snackbar</span>
  <button class="snackbar-action">Action</button>
</div>

## Tables

Tables display sets of data.

```markdown
| Header 1 | Header 2 |
| :------- | :------- |
| Row 1    | Data 1   |
| Row 2    | Data 2   |
```

| Header 1 | Header 2 |
| :------- | :------- |
| Row 1    | Data 1   |
| Row 2    | Data 2   |

## Code Blocks

Code blocks display snippets of code.

```html
<div class="code-block">
  puts "Hello World"
</div>
```
<div class="code-block">
  puts "Hello World"
</div>
