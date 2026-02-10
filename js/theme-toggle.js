(function() {
  var storageKey = "preferred-theme";

  function getSavedTheme() {
    try {
      return localStorage.getItem(storageKey);
    } catch (e) {
      return null;
    }
  }

  function saveTheme(themeName) {
    try {
      localStorage.setItem(storageKey, themeName);
    } catch (e) {
      return;
    }
  }

  function currentTheme() {
    return document.documentElement.classList.contains("theme-dark") ? "dark" : "light";
  }

  function applyTheme(themeName, persist) {
    var normalized = themeName === "dark" ? "dark" : "light";
    document.documentElement.classList.toggle("theme-dark", normalized === "dark");
    updateButton(normalized);
    if (persist) {
      saveTheme(normalized);
    }
  }

  function updateButton(themeName) {
    var button = document.getElementById("theme-toggle");
    if (!button) {
      return;
    }
    var isDark = themeName === "dark";
    button.setAttribute("aria-pressed", isDark ? "true" : "false");
    button.textContent = isDark ? "Dark mode: on" : "Dark mode: off";
  }

  function setupToggle() {
    var button = document.getElementById("theme-toggle");
    if (!button) {
      return;
    }

    var saved = getSavedTheme();
    if (saved === "dark" || saved === "light") {
      applyTheme(saved, false);
    } else {
      updateButton(currentTheme());
    }

    button.addEventListener("click", function() {
      var nextTheme = currentTheme() === "dark" ? "light" : "dark";
      applyTheme(nextTheme, true);
    });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", setupToggle);
  } else {
    setupToggle();
  }
})();
