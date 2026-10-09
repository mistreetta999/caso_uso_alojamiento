// main.js
// Script principal para el sistema de alojamientos

document.addEventListener("DOMContentLoaded", function () {
    console.log("JavaScript cargado correctamente ✅");

    // Toggle de menú
    const menuBtn = document.getElementById("menu-btn");
    const nav = document.getElementById("nav");

    if (menuBtn && nav) {
        menuBtn.addEventListener("click", function () {
            nav.classList.toggle("open");
        });
    }

    // Botón de reserva
    const reservarBtn = document.getElementById("reservar-btn");
    if (reservarBtn) {
        reservarBtn.addEventListener("click", function () {
            alert("Reserva realizada con éxito 🎉");
        });
    }
});
