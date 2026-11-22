# TaskManager-DevOps

Sistema web para la gestión de tareas desarrollado como caso práctico de las fases de DevOps. Permite registrar, consultar, editar y eliminar tareas, además de cambiar su estado y prioridad.

## Funciones

- Registrar tareas con nombre obligatorio, descripción y prioridad Alta, Media o Baja.
- Consultar todas las tareas en una tabla con estado y prioridad.
- Editar el nombre, la descripción y la prioridad de una tarea.
- Eliminar tareas después de confirmar la acción.
- Cambiar el estado entre Pendiente, En proceso y Terminada.
- Verificar el estado de la aplicación y de la base de datos en `/health`.

## Ejecución local

Se requiere Python 3.12 o superior y uv.

```sh
uv sync --locked
uv run python app.py
```

La aplicación queda disponible en http://localhost:5000. La base de datos SQLite se crea en `data/taskmanager.db`; para cambiar la ruta se define la variable de entorno `TASKMANAGER_DB`.

## Pruebas

```sh
uv run pytest -v
```

Las dependencias de producción se exportan a `requirements.txt` con:

```sh
uv export --no-hashes --no-dev -o requirements.txt
```

## Despliegue

La versión publicada está disponible en https://taskmanager-production-143c7d8d.up.railway.app y corresponde al Release https://github.com/netfoor/TaskManager-DevOps/releases/tag/v1.0.0.

La configuración de Railway se documenta en `docs/despliegue.md` y el monitoreo en `docs/monitoreo.md`.

## Planeación

El tablero de trabajo y el seguimiento de actividades están en https://github.com/users/netfoor/projects/2. Las historias de usuario y el plan se encuentran en `docs/historias-usuario.md` y `docs/plan.md`.
