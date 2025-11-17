const API = "http://localhost:5000";

// SWITCH TABS
function showTab(tab) {
    document.querySelectorAll(".tab").forEach(t => t.classList.remove("active"));
    document.getElementById(tab).classList.add("active");
}

// REGISTER
document.querySelector("#register form").addEventListener("submit", async (e) => {
    e.preventDefault();

    const email = document.querySelector("#register input[type=email]").value;
    const password = document.querySelector("#register input[type=password]").value;

    const res = await fetch(API + "/register", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({ email, password })
    });

    alert((await res.json()).message);
});

// LOGIN
document.querySelector("#login form").addEventListener("submit", async (e) => {
    e.preventDefault();

    const email = document.querySelector("#login input[type=email]").value;
    const password = document.querySelector("#login input[type=password]").value;

    const res = await fetch(API + "/login", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({ email, password })
    });

    alert((await res.json()).message);
});