// Main JS
document.addEventListener('DOMContentLoaded', function() {
  // Sidebar Logic
  const menuToggle = document.getElementById('menu-toggle');
  const sidebar = document.querySelector('.sidebar');

  if (menuToggle && sidebar) {
    // Create overlay
    const overlay = document.createElement('div');
    overlay.className = 'sidebar-overlay';
    document.body.appendChild(overlay);

    menuToggle.addEventListener('click', function() {
      sidebar.classList.toggle('open');
      overlay.classList.toggle('active');
    });

    overlay.addEventListener('click', function() {
      sidebar.classList.remove('open');
      overlay.classList.remove('active');
    });
  }

  // Theme Picker Logic
  const themePicker = document.getElementById('theme-picker');
  const html = document.documentElement;
  const storedPalette = localStorage.getItem('theme-palette');

  // Dark Mode Logic
  const darkModeToggle = document.getElementById('dark-mode-toggle');
  const storedDarkMode = localStorage.getItem('theme-dark-mode');

  function updateDarkModeIcon(isDark) {
      if (!darkModeToggle) return;
      const span = darkModeToggle.querySelector('span');
      if (span) {
          span.textContent = isDark ? '☾' : '☀';
      }
  }

  // Init Dark Mode
  if (storedDarkMode === 'true' || (!storedDarkMode && window.matchMedia('(prefers-color-scheme: dark)').matches)) {
      html.classList.add('dark');
      updateDarkModeIcon(true);
  } else {
      updateDarkModeIcon(false);
  }

  if (darkModeToggle) {
      darkModeToggle.addEventListener('click', function() {
          html.classList.toggle('dark');
          const isDark = html.classList.contains('dark');
          localStorage.setItem('theme-dark-mode', isDark);
          updateDarkModeIcon(isDark);
      });
  }

  if (themePicker) {
    // If a palette is stored, apply it
    if (storedPalette) {
      // Remove existing palette classes
      const classes = html.className.split(' ').filter(c => !c.startsWith('palette-'));
      html.className = classes.join(' ') + ' ' + storedPalette;

      // Update picker value
      themePicker.value = storedPalette;
    } else {
      // If no stored palette, sync picker with current html class (server-side default)
      const currentPalette = html.className.split(' ').find(c => c.startsWith('palette-'));
      if (currentPalette) {
        themePicker.value = currentPalette;
      }
    }

    // Listen for changes
    themePicker.addEventListener('change', function() {
      const newPalette = this.value;

      // Remove existing palette classes
      const classes = html.className.split(' ').filter(c => !c.startsWith('palette-'));
      html.className = classes.join(' ') + ' ' + newPalette;

      // Save to localStorage
      localStorage.setItem('theme-palette', newPalette);
    });
  }

  // Auto-expand Sidebar
  const activeLink = document.querySelector('.nav-link.active');
  if (activeLink) {
    let parent = activeLink.closest('details');
    while (parent) {
      parent.setAttribute('open', '');
      parent = parent.parentElement.closest('details');
    }
  }

  console.log('Materialistic Jekyll Theme Loaded');
});
