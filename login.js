// Cookie banner interactions
document.getElementById("close-btn").addEventListener("click", () => {
    document.querySelector(".cookie-banner").style.display = "none";
});

document.getElementById("manage-btn").addEventListener("click", () => {
    alert("Cookie management options coming soon!");
});

// Sign-in button action
document.getElementById("sign-in").addEventListener("click", () => {
    // Navigate to signin.html
    window.location.href = "signin.html";
});
