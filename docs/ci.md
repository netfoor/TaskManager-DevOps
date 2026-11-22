# Integración continua

El archivo `.github/workflows/ci.yml` define el workflow `Integracion Continua`. Se ejecuta en cada push a `main` y en cada Pull Request con `main` como rama base. El job `pruebas` descarga el código con `actions/checkout@v7.0.1`, instala uv con `astral-sh/setup-uv@v10.4.0`, sincroniza el entorno con `uv sync --locked` y ejecuta `uv run pytest -v`.

## Ejecución fallida real

- Run: 45051866776
- Enlace: https://github.com/netfoor/TaskManager-DevOps/actions/runs/45051866776
- Origen: Pull Request #21, rama `chore/estructura-inicial`.
- Resultado: 1 prueba fallida y 4 aprobadas.
- Prueba afectada: `test_listado_muestra_la_tarea_mas_reciente_primero`.
- Causa: `obtener_tareas()` devolvía los registros con `ORDER BY id ASC`, por lo que la tarea más antigua aparecía primero en la página principal. La aserción `cuerpo.index("Segunda") < cuerpo.index("Primera")` falló con `assert 1468 < 1058`.
- Corrección: se cambió la consulta a `ORDER BY id DESC` en `app.py` y se confirmó con `uv run pytest -v` en local antes de subir el cambio a la misma rama.
- Salida de la ejecución: `.remedial/evidencias/ci_run_45051866776_fallo.log`.

## Ejecución corregida

- Run: 45051957172
- Enlace: https://github.com/netfoor/TaskManager-DevOps/actions/runs/45051957172
- Resultado: 5 pruebas aprobadas.
- Salida local de la corrección: `.remedial/evidencias/pytest_estructura_corregido.txt`.

La falla se detectó antes de integrar el código a `main`, lo que muestra que el workflow cumple su función de bloquear cambios que no pasan las pruebas.
