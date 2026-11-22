"""Aplicación web TaskManager para la gestión de tareas."""

from __future__ import annotations

import os
import sqlite3
from pathlib import Path

from flask import Flask, current_app, g, jsonify, render_template

BASE_DIR = Path(__file__).resolve().parent
ESTADOS = ("Pendiente", "En proceso", "Terminada")
PRIORIDADES = ("Alta", "Media", "Baja")


def ruta_base_datos() -> str:
    """Devuelve la ruta SQLite configurada o la ruta local por omisión."""
    return os.environ.get("TASKMANAGER_DB", str(BASE_DIR / "data" / "taskmanager.db"))


def get_db() -> sqlite3.Connection:
    """Abre y reutiliza una conexión SQLite dentro del contexto de la petición."""
    if "db" not in g:
        ruta = Path(current_app.config["DATABASE"])
        ruta.parent.mkdir(parents=True, exist_ok=True)
        g.db = sqlite3.connect(ruta)
        g.db.row_factory = sqlite3.Row
    return g.db


def cerrar_db(_error: object = None) -> None:
    """Cierra la conexión al terminar la petición."""
    conexion = g.pop("db", None)
    if conexion is not None:
        conexion.close()


def inicializar_db() -> None:
    """Crea la tabla de tareas si todavía no existe."""
    ruta = Path(current_app.config["DATABASE"])
    ruta.parent.mkdir(parents=True, exist_ok=True)
    with sqlite3.connect(ruta) as conexion:
        conexion.execute(
            """
            CREATE TABLE IF NOT EXISTS tareas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                descripcion TEXT NOT NULL DEFAULT '',
                estado TEXT NOT NULL DEFAULT 'Pendiente'
                    CHECK (estado IN ('Pendiente', 'En proceso', 'Terminada')),
                prioridad TEXT NOT NULL DEFAULT 'Media'
                    CHECK (prioridad IN ('Alta', 'Media', 'Baja')),
                creado_en TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
            )
            """
        )


def obtener_tareas() -> list[sqlite3.Row]:
    """Devuelve todas las tareas, de la más reciente a la más antigua."""
    return get_db().execute("SELECT * FROM tareas ORDER BY id DESC").fetchall()


def base_disponible() -> bool:
    """Comprueba que la base de datos responda a una consulta simple."""
    try:
        get_db().execute("SELECT 1").fetchone()
    except sqlite3.Error:
        return False
    return True


def listar_plantillas(carpeta: str) -> list[str]:
    """Lista las plantillas parciales que agregan acciones a la interfaz."""
    directorio = BASE_DIR / "templates" / carpeta
    if not directorio.exists():
        return []
    return [f"{carpeta}/{archivo.name}" for archivo in sorted(directorio.glob("*.html"))]


def listar_scripts() -> list[str]:
    """Lista los módulos JavaScript agregados por cada funcionalidad."""
    directorio = BASE_DIR / "static" / "js" / "modulos"
    if not directorio.exists():
        return []
    return [f"modulos/{archivo.name}" for archivo in sorted(directorio.glob("*.js"))]


def crear_app(configuracion: dict | None = None) -> Flask:
    """Construye la aplicación Flask y registra los módulos disponibles."""
    aplicacion = Flask(__name__)
    aplicacion.config["DATABASE"] = ruta_base_datos()
    if configuracion:
        aplicacion.config.update(configuracion)

    with aplicacion.app_context():
        inicializar_db()

    aplicacion.teardown_appcontext(cerrar_db)
    aplicacion.jinja_env.globals["acciones_globales"] = lambda: listar_plantillas("acciones/globales")
    aplicacion.jinja_env.globals["acciones_fila"] = lambda: listar_plantillas("acciones/fila")
    aplicacion.jinja_env.globals["scripts_modulo"] = listar_scripts

    from routes import registrar_blueprints

    registrar_blueprints(aplicacion)

    @aplicacion.get("/")
    def indice():
        return render_template("index.html", tareas=obtener_tareas())

    @aplicacion.get("/health")
    def health():
        disponible = base_disponible()
        cuerpo = {
            "estado": "ok" if disponible else "error",
            "base_de_datos": "disponible" if disponible else "no disponible",
            "ruta": aplicacion.config["DATABASE"],
        }
        return jsonify(cuerpo), 200 if disponible else 503

    return aplicacion


app = crear_app()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", "5000")))
