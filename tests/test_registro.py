"""Pruebas del registro de tareas."""

from app import get_db
from routes.registro import insertar_tarea, validar_registro


def test_registro_valido_guarda_tarea(cliente, aplicacion):
    respuesta = cliente.post(
        "/tareas",
        data={"nombre": "Elaborar documentacion", "descripcion": "Entregar el manual", "prioridad": "Alta"},
        follow_redirects=True,
    )

    with aplicacion.app_context():
        tarea = get_db().execute("SELECT * FROM tareas WHERE nombre = ?", ("Elaborar documentacion",)).fetchone()

    assert respuesta.status_code == 200
    assert "La tarea se registró correctamente." in respuesta.get_data(as_text=True)
    assert tarea is not None
    assert tarea["descripcion"] == "Entregar el manual"
    assert tarea["prioridad"] == "Alta"
    assert tarea["estado"] == "Pendiente"


def test_registro_sin_nombre_muestra_error(cliente, aplicacion):
    respuesta = cliente.post(
        "/tareas",
        data={"nombre": "   ", "descripcion": "Sin nombre", "prioridad": "Media"},
        follow_redirects=True,
    )

    with aplicacion.app_context():
        total = get_db().execute("SELECT COUNT(*) FROM tareas").fetchone()[0]

    assert "El nombre de la tarea es obligatorio." in respuesta.get_data(as_text=True)
    assert total == 0


def test_registro_rechaza_prioridad_invalida(cliente, aplicacion):
    respuesta = cliente.post(
        "/tareas",
        data={"nombre": "Tarea valida", "descripcion": "", "prioridad": "Urgente"},
        follow_redirects=True,
    )

    with aplicacion.app_context():
        total = get_db().execute("SELECT COUNT(*) FROM tareas").fetchone()[0]

    assert "Selecciona una prioridad válida" in respuesta.get_data(as_text=True)
    assert total == 0


def test_insertar_tarea_devuelve_identificador(aplicacion):
    with aplicacion.app_context():
        identificador = insertar_tarea("  Revisar servidor  ", " Revisar estado ", "Baja")
        tarea = get_db().execute("SELECT * FROM tareas WHERE id = ?", (identificador,)).fetchone()

    assert tarea["nombre"] == "Revisar servidor"
    assert tarea["descripcion"] == "Revisar estado"


def test_validar_registro_acepta_datos_correctos():
    assert validar_registro("Tarea", "Media") is None
