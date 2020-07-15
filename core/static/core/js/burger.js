function openBurger() {
    let sidebar = document.getElementById("sidebar");
    let closeWrapper = document.getElementById("close-wrapper");
    sidebar.className = "sidebar mobile"
    closeWrapper.className = "close-wrapper active"
}

function closeBurger() {
    let sidebar = document.getElementById("sidebar");
    let closeWrapper = document.getElementById("close-wrapper");
    sidebar.className = "sidebar"
    closeWrapper.className = "close-wrapper"
}