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
- Salida de la ejecución: https://github.com/netfoor/TaskManager-DevOps/actions/runs/45051866776.

## Ejecución corregida

- Run: 45051957172
- Enlace: https://github.com/netfoor/TaskManager-DevOps/actions/runs/45051957172
- Resultado: 5 pruebas aprobadas.
- La corrección se verificó de nuevo en el run https://github.com/netfoor/TaskManager-DevOps/actions/runs/45051957172.

La falla se detectó antes de integrar el código a `main`, lo que muestra que el workflow cumple su función de bloquear cambios que no pasan las pruebas.

## Ejecuciones posteriores

Todos los Pull Requests integrados pasaron la integración continua antes de llegar a `main`:

| PR | Rama | Run |
| --- | --- | --- |
| #22 | `feature/registro-tareas` | [45052578947](https://github.com/netfoor/TaskManager-DevOps/actions/runs/45052578947) |
| #23 | `feature/editar-tareas` | [45052581616](https://github.com/netfoor/TaskManager-DevOps/actions/runs/45052581616) |
| #24 | `feature/eliminar-tareas` | [45052587354](https://github.com/netfoor/TaskManager-DevOps/actions/runs/45052587354) |
| #25 | `feature/estado-prioridad` | [45052589214](https://github.com/netfoor/TaskManager-DevOps/actions/runs/45052589214) |
| #27 | `fix/editar-inexistente` | [45054946943](https://github.com/netfoor/TaskManager-DevOps/actions/runs/45054946943) |
| #32 | `docs/entrega-monitoreo` | [45054954056](https://github.com/netfoor/TaskManager-DevOps/actions/runs/45054954056) |
| #33 | `chore/gunicorn` | [45054963764](https://github.com/netfoor/TaskManager-DevOps/actions/runs/45054963764) |
| #34 | `ci/monitoreo-6h` | [45056229980](https://github.com/netfoor/TaskManager-DevOps/actions/runs/45056229980) |
| #36 | `fix/monitoreo-shell` | [45057501621](https://github.com/netfoor/TaskManager-DevOps/actions/runs/45057501621) |

Después de las integraciones, `main` volvió a pasar con 26 pruebas, por ejemplo en los runs [45055567240](https://github.com/netfoor/TaskManager-DevOps/actions/runs/45055567240), [45056458896](https://github.com/netfoor/TaskManager-DevOps/actions/runs/45056458896) y [45057709595](https://github.com/netfoor/TaskManager-DevOps/actions/runs/45057709595).

La entrega continua se ejecutó al publicar `v1.0.0` en el run [45055670829](https://github.com/netfoor/TaskManager-DevOps/actions/runs/45055670829) y terminó en success.
