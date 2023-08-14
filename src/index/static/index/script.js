const hamburguer = document.querySelector(".hamburguer");
const navmenu = document.querySelector(".nav-menu"); // Removido o "active" aqui

hamburguer.addEventListener("click", () => {
    hamburguer.classList.toggle('active');
    navmenu.classList.toggle('active');
});




  