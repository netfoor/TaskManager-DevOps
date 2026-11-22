"""Pruebas de la eliminación de tareas."""

from app import get_db
from routes.eliminacion import eliminar_tarea


def crear_tarea(aplicacion, nombre="Tarea a eliminar"):
    with aplicacion.app_context():
        conexion = get_db()
        cursor = conexion.execute("INSERT INTO tareas (nombre) VALUES (?)", (nombre,))
        conexion.commit()
        return int(cursor.lastrowid)


def test_eliminar_tarea_reduce_el_listado(cliente, aplicacion):
    identificador = crear_tarea(aplicacion)

    respuesta = cliente.post(f"/tareas/{identificador}/eliminar", follow_redirects=True)

    with aplicacion.app_context():
        restante = get_db().execute("SELECT COUNT(*) FROM tareas").fetchone()[0]

    assert respuesta.status_code == 200
    assert "La tarea se eliminó correctamente." in respuesta.get_data(as_text=True)
    assert "Tarea a eliminar" not in respuesta.get_data(as_text=True)
    assert restante == 0


def test_eliminar_tarea_inexistente_muestra_error(cliente):
    respuesta = cliente.post("/tareas/9999/eliminar", follow_redirects=True)

    assert "No se encontró la tarea solicitada." in respuesta.get_data(as_text=True)


def test_eliminar_tarea_no_acepta_get(cliente, aplicacion):
    identificador = crear_tarea(aplicacion)

    assert cliente.get(f"/tareas/{identificador}/eliminar").status_code == 405


def test_eliminar_tarea_devuelve_resultado(aplicacion):
    identificador = crear_tarea(aplicacion)

    with aplicacion.app_context():
        assert eliminar_tarea(identificador) is True
        assert eliminar_tarea(identificador) is False
