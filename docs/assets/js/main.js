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

  console.log('Materialistic Jekyll Theme Loaded');
});
