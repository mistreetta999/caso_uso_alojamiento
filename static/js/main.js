// static/js/main.js

// Esperar a que el DOM esté listo
document.addEventListener("DOMContentLoaded", function () {
    console.log("main.js cargado correctamente ✅");

    // Ejemplo: toggle de menú
    const menuBtn = document.getElementById("menu-btn");
    const nav = document.getElementById("nav");

    if (menuBtn && nav) {
        menuBtn.addEventListener("click", () => {
            nav.classList.toggle("open");
        });
    }

    // Ejemplo: alerta de prueba
    const testBtn = document.getElementById("test-btn");
    if (testBtn) {
        testBtn.addEventListener("click", () => {
            alert("Botón funcionando 🎮");
        });
    }
});
