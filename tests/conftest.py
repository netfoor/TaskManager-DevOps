"""Fixtures compartidas por las pruebas de TaskManager."""

import pytest

from app import crear_app


@pytest.fixture
def aplicacion(tmp_path):
    return crear_app(
        {
            "DATABASE": str(tmp_path / "tareas.db"),
            "TESTING": True,
        }
    )


@pytest.fixture
def cliente(aplicacion):
    return aplicacion.test_client()
