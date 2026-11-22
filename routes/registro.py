"""Registro de tareas nuevas (RF01)."""

from __future__ import annotations

from flask import Blueprint, flash, redirect, request, url_for

from app import PRIORIDADES, get_db

bp = Blueprint("registro", __name__)


def validar_registro(nombre: str, prioridad: str) -> str | None:
    """Devuelve un mensaje de error cuando los datos no son válidos."""
    if not nombre.strip():
        return "El nombre de la tarea es obligatorio."
    if prioridad not in PRIORIDADES:
        return "Selecciona una prioridad válida: Alta, Media o Baja."
    return None


def insertar_tarea(nombre: str, descripcion: str, prioridad: str) -> int:
    """Guarda una tarea y devuelve el identificador asignado."""
    conexion = get_db()
    cursor = conexion.execute(
        "INSERT INTO tareas (nombre, descripcion, prioridad) VALUES (?, ?, ?)",
        (nombre.strip(), descripcion.strip(), prioridad),
    )
    conexion.commit()
    return int(cursor.lastrowid)


@bp.post("/tareas")
def registrar_tarea():
    nombre = request.form.get("nombre", "")
    descripcion = request.form.get("descripcion", "")
    prioridad = request.form.get("prioridad", "Media")

    error = validar_registro(nombre, prioridad)
    if error:
        flash(error, "error")
        return redirect(url_for("indice"))

    insertar_tarea(nombre, descripcion, prioridad)
    flash("La tarea se registró correctamente.", "success")
    return redirect(url_for("indice"))
