"""Pruebas unitarias de la estructura base de TaskManager."""

from app import get_db, obtener_tareas


def test_pagina_principal_sin_tareas(cliente):
    respuesta = cliente.get("/")

    assert respuesta.status_code == 200
    assert "Todavía no hay tareas registradas." in respuesta.get_data(as_text=True)


def test_ruta_de_base_configurable(aplicacion, tmp_path):
    assert aplicacion.config["DATABASE"] == str(tmp_path / "tareas.db")


def test_health_verifica_base(cliente):
    respuesta = cliente.get("/health")

    assert respuesta.status_code == 200
    assert respuesta.get_json()["estado"] == "ok"
    assert respuesta.get_json()["base_de_datos"] == "disponible"


def test_obtener_tareas_devuelve_registros(cliente, aplicacion):
    with aplicacion.app_context():
        get_db().execute(
            "INSERT INTO tareas (nombre, descripcion) VALUES (?, ?)",
            ("Elaborar documentacion", "Descripcion de prueba"),
        )
        get_db().commit()
        tareas = obtener_tareas()

    assert len(tareas) == 1
    assert tareas[0]["nombre"] == "Elaborar documentacion"
    assert tareas[0]["estado"] == "Pendiente"
    assert tareas[0]["prioridad"] == "Media"


def test_listado_muestra_la_tarea_mas_reciente_primero(cliente, aplicacion):
    with aplicacion.app_context():
        get_db().execute("INSERT INTO tareas (nombre) VALUES ('Primera')")
        get_db().execute("INSERT INTO tareas (nombre) VALUES ('Segunda')")
        get_db().commit()

    respuesta = cliente.get("/")
    cuerpo = respuesta.get_data(as_text=True)

    assert cuerpo.index("Segunda") < cuerpo.index("Primera")
