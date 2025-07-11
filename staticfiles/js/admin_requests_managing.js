const members = [
  {
    profile: "images/man.jpg",
    nin: "123456789",
    name: "Amina Larbi",
    gender: "Female",
    age: 96,
    email: "aminalarbi@gmail.com",
    municipal: "Miliana",
    phase: "Rejected",
    contact: "0696449951",
    participation: 10,
  },
  {
    profile: "images/man.jpg",
    nin: "258369147",
    name: "Amine Tounsi",
    gender: "Female",
    age: 26,
    email: "aminetounsi@gmail.com",
    municipal: "Miliana",
    phase: "Accepted",
    contact: "0556263501",
    participation: 26,
  },
  // Ajouter d'autres utilisateurs ici...
];

const tableBody = document.getElementById("memberTableBody");

function renderMembers() {
  tableBody.innerHTML = "";
  members.forEach((user) => {
    const row = document.createElement("tr");

    row.innerHTML = `
      <td><img src="${user.profile}" alt="Profile" style="width: 40px; border-radius: 50%;"></td>
      <td>${user.nin}</td>
      <td>${user.name}</td>
      <td>${user.gender}</td>
      <td>${user.age}</td>
      <td>${user.email}</td>
      <td>${user.municipal}</td>
      <td><span class="status ${user.phase.toLowerCase()}">${user.phase}</span></td>
      <td>${user.contact}</td>
      <td>${user.participation}</td>
    `;

    tableBody.appendChild(row);
  });
}

renderMembers();
