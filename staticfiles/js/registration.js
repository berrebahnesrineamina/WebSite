document.addEventListener("DOMContentLoaded", function () {
  const form = document.getElementById("registrationForm");

  if (form) {
    form.addEventListener("submit", function (e) {
      // Supprime ceci si tu veux que le formulaire soit soumis normalement
      // e.preventDefault(); 
      
      // Optionnel : pour afficher une alerte sans empêcher la soumission
      alert("Registration submitted!");
    });
  } else {
    console.log("Form not found!");
  }
});
