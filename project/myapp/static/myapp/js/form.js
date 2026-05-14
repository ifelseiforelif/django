const form = document.getElementById("form");
const p = document.getElementById("data");
form.addEventListener("submit", (e) => {
  e.preventDefault();
  const data = Object.fromEntries(new FormData(form).entries());
  fetch("/", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(data),
  })
    .then((response) => response.json())
    .then((data) => {
      form.reset();
      window.location.reload();
    })
    .catch((error) => console.error("Error:", error));
});
