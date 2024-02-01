document.addEventListener('DOMContentLoaded', function() {
  // Check for the theme in localStorage and apply it on page load
//   const selectedTheme = localStorage.getItem('selectedTheme');
//   if (selectedTheme) {
//     applyTheme(selectedTheme);
//   }
});

function applyTheme(theme) {
  // Remove existing theme classes
  document.body.classList.remove('blue-theme', 'red-theme', 'green-theme', 'yellow-theme', 'pink-theme');

  // Add the selected theme class
  document.body.style.backgroundColor = 'black';
  document.body.style.color = getFontColor(theme);

  // Save the selected theme to localStorage
//   localStorage.setItem('selectedTheme', theme);
}

function getFontColor(theme) {
    // Define font colors for each theme
    const fontColors = {
      'blue-theme': 'blue',   // Change this to your desired font color for the blue theme
      'red-theme': 'red',
      'green-theme': 'rgb(15, 233, 7)',
      'yellow-theme': 'yellow',
      'pink-theme': 'rgb(240, 40, 213)'
      // Add more themes and font colors as needed
    };
  
    // Return the font color for the given theme
    return fontColors[theme];  // Default to white if the theme is not found
  }
function changeTheme(theme) {
  applyTheme(theme);
}
