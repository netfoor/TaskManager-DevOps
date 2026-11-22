"""Eliminación de tareas (RF04)."""

from __future__ import annotations

from flask import Blueprint, flash, redirect, url_for

from app import get_db

bp = Blueprint("eliminacion", __name__)


def eliminar_tarea(identificador: int) -> bool:
    """Elimina una tarea y devuelve True si existía."""
    conexion = get_db()
    cursor = conexion.execute("DELETE FROM tareas WHERE id = ?", (identificador,))
    conexion.commit()
    return cursor.rowcount > 0


@bp.post("/tareas/<int:identificador>/eliminar")
def borrar_tarea(identificador: int):
    if eliminar_tarea(identificador):
        flash("La tarea se eliminó correctamente.", "success")
    else:
        flash("No se encontró la tarea solicitada.", "error")
    return redirect(url_for("indice"))
