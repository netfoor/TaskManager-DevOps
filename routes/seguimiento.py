"""Cambio de estado y asignación de prioridad (RF05 y RF06)."""

from __future__ import annotations

from flask import Blueprint, flash, redirect, request, url_for

from app import ESTADOS, PRIORIDADES, get_db

bp = Blueprint("seguimiento", __name__)


def cambiar_campo(identificador: int, columna: str, valor: str, valores_validos: tuple[str, ...]) -> bool:
    """Actualiza estado o prioridad después de validar el valor recibido."""
    if valor not in valores_validos:
        return False
    conexion = get_db()
    cursor = conexion.execute(
        f"UPDATE tareas SET {columna} = ? WHERE id = ?",
        (valor, identificador),
    )
    conexion.commit()
    return cursor.rowcount > 0


@bp.post("/tareas/<int:identificador>/estado")
def cambiar_estado(identificador: int):
    estado = request.form.get("estado", "")

    if cambiar_campo(identificador, "estado", estado, ESTADOS):
        flash("El estado de la tarea se actualizó correctamente.", "success")
    else:
        flash("Selecciona un estado válido: Pendiente, En proceso o Terminada.", "error")

    return redirect(url_for("indice"))


@bp.post("/tareas/<int:identificador>/prioridad")
def cambiar_prioridad(identificador: int):
    prioridad = request.form.get("prioridad", "")

    if cambiar_campo(identificador, "prioridad", prioridad, PRIORIDADES):
        flash("La prioridad de la tarea se actualizó correctamente.", "success")
    else:
        flash("Selecciona una prioridad válida: Alta, Media o Baja.", "error")

    return redirect(url_for("indice"))
