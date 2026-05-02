const form = document.getElementById("form");
const p = document.getElementById("data");
form.addEventListener("submit", (e) => {
  e.preventDefault();
  const data = Object.fromEntries(new FormData(form).entries());
  console.log(data);
  fetch("/", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(data),
  })
    .then((response) => response.json())
    .then((data) => {
      p.innerHTML = data.name + " " + data.email;
      form.reset();
    })
    .catch((error) => console.error("Error:", error));
});
