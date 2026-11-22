"""Pruebas de la edición de tareas."""

from app import get_db
from routes.edicion import actualizar_tarea, obtener_tarea


def crear_tarea(aplicacion, nombre="Tarea original", estado="En proceso"):
    with aplicacion.app_context():
        conexion = get_db()
        cursor = conexion.execute(
            "INSERT INTO tareas (nombre, descripcion, estado, prioridad) VALUES (?, ?, ?, ?)",
            (nombre, "Descripcion original", estado, "Media"),
        )
        conexion.commit()
        return int(cursor.lastrowid)


def test_formulario_de_edicion_carga_datos(cliente, aplicacion):
    identificador = crear_tarea(aplicacion)

    respuesta = cliente.get(f"/tareas/{identificador}/editar")
    cuerpo = respuesta.get_data(as_text=True)

    assert respuesta.status_code == 200
    assert "Tarea original" in cuerpo
    assert "Descripcion original" in cuerpo
    assert 'value="Media" selected' in cuerpo


def test_edicion_actualiza_nombre_descripcion_y_prioridad(cliente, aplicacion):
    identificador = crear_tarea(aplicacion)

    respuesta = cliente.post(
        f"/tareas/{identificador}/editar",
        data={"nombre": "Tarea editada", "descripcion": "Nueva descripcion", "prioridad": "Alta"},
        follow_redirects=True,
    )

    with aplicacion.app_context():
        tarea = obtener_tarea(identificador)

    assert respuesta.status_code == 200
    assert "La tarea se actualizó correctamente." in respuesta.get_data(as_text=True)
    assert tarea["nombre"] == "Tarea editada"
    assert tarea["descripcion"] == "Nueva descripcion"
    assert tarea["prioridad"] == "Alta"
    assert tarea["estado"] == "En proceso"


def test_edicion_sin_nombre_muestra_error(cliente, aplicacion):
    identificador = crear_tarea(aplicacion)

    respuesta = cliente.post(
        f"/tareas/{identificador}/editar",
        data={"nombre": "  ", "descripcion": "Cambio", "prioridad": "Baja"},
        follow_redirects=True,
    )

    with aplicacion.app_context():
        tarea = obtener_tarea(identificador)

    assert "El nombre de la tarea es obligatorio." in respuesta.get_data(as_text=True)
    assert tarea["nombre"] == "Tarea original"


def test_edicion_rechaza_prioridad_invalida(cliente, aplicacion):
    identificador = crear_tarea(aplicacion)

    respuesta = cliente.post(
        f"/tareas/{identificador}/editar",
        data={"nombre": "Tarea", "descripcion": "", "prioridad": "Urgente"},
        follow_redirects=True,
    )

    assert "Selecciona una prioridad válida" in respuesta.get_data(as_text=True)


def test_editar_tarea_inexistente_devuelve_404(cliente):
    assert cliente.get("/tareas/9999/editar").status_code == 404


def test_actualizar_tarea_devuelve_falso_sin_registros(aplicacion):
    with aplicacion.app_context():
        assert actualizar_tarea(9999, "Inexistente", "", "Baja") is False
