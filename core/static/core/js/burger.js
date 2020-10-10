function openBurger() {
    let sidebar = document.getElementById("sidebar");
    sidebar.className = sidebar.className.replace("dn", "dib");
}

function closeBurger() {
    let sidebar = document.getElementById("sidebar");
    sidebar.className = sidebar.className.replace("dib", "dn");
}