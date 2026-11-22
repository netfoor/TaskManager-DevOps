"""Pruebas del cambio de estado y de prioridad."""

from app import get_db
from routes.seguimiento import cambiar_campo


def crear_tarea(aplicacion):
    with aplicacion.app_context():
        conexion = get_db()
        cursor = conexion.execute(
            "INSERT INTO tareas (nombre, estado, prioridad) VALUES (?, ?, ?)",
            ("Tarea de prueba", "Pendiente", "Media"),
        )
        conexion.commit()
        return int(cursor.lastrowid)


def leer_tarea(aplicacion, identificador):
    with aplicacion.app_context():
        return get_db().execute("SELECT * FROM tareas WHERE id = ?", (identificador,)).fetchone()


def test_cambiar_estado_valido(cliente, aplicacion):
    identificador = crear_tarea(aplicacion)

    respuesta = cliente.post(
        f"/tareas/{identificador}/estado",
        data={"estado": "Terminada"},
        follow_redirects=True,
    )

    assert "El estado de la tarea se actualizó correctamente." in respuesta.get_data(as_text=True)
    assert leer_tarea(aplicacion, identificador)["estado"] == "Terminada"
    assert "Terminada" in respuesta.get_data(as_text=True)


def test_cambiar_estado_invalido(cliente, aplicacion):
    identificador = crear_tarea(aplicacion)

    respuesta = cliente.post(
        f"/tareas/{identificador}/estado",
        data={"estado": "Cancelada"},
        follow_redirects=True,
    )

    assert "Selecciona un estado válido" in respuesta.get_data(as_text=True)
    assert leer_tarea(aplicacion, identificador)["estado"] == "Pendiente"


def test_cambiar_prioridad_valida(cliente, aplicacion):
    identificador = crear_tarea(aplicacion)

    respuesta = cliente.post(
        f"/tareas/{identificador}/prioridad",
        data={"prioridad": "Alta"},
        follow_redirects=True,
    )

    assert "La prioridad de la tarea se actualizó correctamente." in respuesta.get_data(as_text=True)
    assert leer_tarea(aplicacion, identificador)["prioridad"] == "Alta"
    assert "etiqueta--alta" in respuesta.get_data(as_text=True)


def test_cambiar_prioridad_invalida(cliente, aplicacion):
    identificador = crear_tarea(aplicacion)

    respuesta = cliente.post(
        f"/tareas/{identificador}/prioridad",
        data={"prioridad": "Urgente"},
        follow_redirects=True,
    )

    assert "Selecciona una prioridad válida" in respuesta.get_data(as_text=True)
    assert leer_tarea(aplicacion, identificador)["prioridad"] == "Media"


def test_cambiar_campo_valida_los_valores_permitidos(aplicacion):
    identificador = crear_tarea(aplicacion)

    with aplicacion.app_context():
        assert cambiar_campo(identificador, "estado", "En proceso", ("Pendiente", "En proceso", "Terminada")) is True
        assert cambiar_campo(identificador, "estado", "Otro", ("Pendiente", "En proceso", "Terminada")) is False
