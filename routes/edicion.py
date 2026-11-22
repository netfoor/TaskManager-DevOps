"""Edición de tareas existentes (RF03)."""

from __future__ import annotations

from flask import Blueprint, flash, redirect, render_template, request, url_for

from app import PRIORIDADES, get_db

bp = Blueprint("edicion", __name__)


def obtener_tarea(identificador: int):
    """Devuelve una tarea por su identificador."""
    return get_db().execute("SELECT * FROM tareas WHERE id = ?", (identificador,)).fetchone()


def actualizar_tarea(identificador: int, nombre: str, descripcion: str, prioridad: str) -> bool:
    """Actualiza nombre, descripción y prioridad sin modificar el estado."""
    conexion = get_db()
    cursor = conexion.execute(
        """
        UPDATE tareas
        SET nombre = ?, descripcion = ?, prioridad = ?
        WHERE id = ?
        """,
        (nombre.strip(), descripcion.strip(), prioridad, identificador),
    )
    conexion.commit()
    return cursor.rowcount > 0


@bp.route("/tareas/<int:identificador>/editar", methods=["GET", "POST"])
def editar_tarea(identificador: int):
    if request.method == "POST":
        if obtener_tarea(identificador) is None:
            flash("No se encontró la tarea solicitada.", "error")
            return redirect(url_for("indice"))

        nombre = request.form.get("nombre", "")
        descripcion = request.form.get("descripcion", "")
        prioridad = request.form.get("prioridad", "Media")

        if not nombre.strip():
            flash("El nombre de la tarea es obligatorio.", "error")
        elif prioridad not in PRIORIDADES:
            flash("Selecciona una prioridad válida: Alta, Media o Baja.", "error")
        else:
            actualizar_tarea(identificador, nombre, descripcion, prioridad)
            flash("La tarea se actualizó correctamente.", "success")
            return redirect(url_for("indice"))

        return redirect(url_for("edicion.editar_tarea", identificador=identificador))

    tarea = obtener_tarea(identificador)
    if tarea is None:
        flash("No se encontró la tarea solicitada.", "error")
        return redirect(url_for("indice")), 404

    return render_template("editar.html", tarea=tarea, prioridades=PRIORIDADES)
