document.addEventListener("DOMContentLoaded", () => {
  const formulario = document.querySelector(".formulario-registro form");
  if (!formulario) return;

  const nombre = formulario.querySelector('input[name="nombre"]');
  nombre.addEventListener("input", () => {
    nombre.setCustomValidity(nombre.value.trim() === "" ? "Escribe el nombre de la tarea." : "");
  });
});
