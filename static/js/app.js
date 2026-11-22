document.addEventListener("DOMContentLoaded", () => {
  document.querySelectorAll("form[data-confirma]").forEach((formulario) => {
    formulario.addEventListener("submit", (evento) => {
      const mensaje = formulario.dataset.confirma;
      if (!window.confirm(mensaje)) {
        evento.preventDefault();
      }
    });
  });

  const avisos = document.querySelectorAll(".aviso");
  if (avisos.length > 0) {
    avisos[0].scrollIntoView({ behavior: "smooth", block: "nearest" });
  }
});
