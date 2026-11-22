"""Descubrimiento automático de los módulos de rutas de TaskManager."""

from __future__ import annotations

import importlib
from pathlib import Path

from flask import Flask


def registrar_blueprints(aplicacion: Flask) -> None:
    """Registra como blueprint cada módulo de la carpeta routes que exporte bp."""
    directorio = Path(__file__).resolve().parent
    for archivo in sorted(directorio.glob("*.py")):
        if archivo.name == "__init__.py":
            continue
        modulo = importlib.import_module(f"routes.{archivo.stem}")
        blueprint = getattr(modulo, "bp", None)
        if blueprint is not None:
            aplicacion.register_blueprint(blueprint)
