document.getElementById("loginForm").addEventListener("submit", function (e) {
  e.preventDefault();

  const email = document.getElementById("email").value;
  const password = document.getElementById("password").value;
  const remember = document.getElementById("remember").checked;

  // Simulation
  alert(`Email: ${email}\nPassword: ${password}\nRemember Me: ${remember}`);
});
