# Plan del proyecto

## Objetivo

Desarrollar TaskManager, un sistema web para administrar las tareas de los empleados de TechSolutions, y aplicar las fases del ciclo de vida DevOps con GitHub como plataforma principal: planeación, desarrollo, integración continua, pruebas, entrega continua, despliegue y monitoreo.

## Requerimientos funcionales

| Código | Funcionalidad | Descripción |
| --- | --- | --- |
| RF01 | Registrar tareas | Permitir agregar nuevas tareas con nombre, descripción y prioridad. |
| RF02 | Consultar tareas | Mostrar todas las tareas registradas. |
| RF03 | Editar tareas | Modificar la información de una tarea. |
| RF04 | Eliminar tareas | Eliminar tareas existentes. |
| RF05 | Cambiar estado | Cambiar entre Pendiente, En proceso y Terminada. |
| RF06 | Asignar prioridad | Clasificar tareas como Alta, Media o Baja. |

## Requerimientos técnicos

- Python 3.12, Flask y SQLite; dependencias administradas con uv y exportadas a requirements.txt.
- Interfaz con HTML, CSS y JavaScript.
- Pruebas unitarias con pytest y ejecución automática en GitHub Actions.
- Base de datos en una ruta configurable mediante la variable de entorno TASKMANAGER_DB.
- Despliegue de la aplicación en Railway con gunicorn y volumen persistente.

## Distribución de responsabilidades

| Integrante | Rol | Responsabilidades |
| --- | --- | --- |
| Fortino Romero Mantilla | Product Owner e Ingeniero DevOps/QA | Requerimientos, prioridades, estructura inicial, integración continua, entrega, despliegue, monitoreo y documentación. |
| Israel Jesús García Osorio | Desarrollador 1 | Registro de tareas, edición de tareas, prioridad y revisiones de código. |
| Luis Joel Gómez Herrera | Desarrollador 2 | Diseño de interfaz, cambio de estado y ejecución de pruebas funcionales. |

Todos los integrantes participan en la revisión de los cambios y conocen las siete fases del proceso.

## Tablero y seguimiento

El proyecto `TaskManager-DevOps` usa una vista Board con las columnas Backlog, To Do, In Progress, Review y Done. Cada issue lleva Prioridad, Estimación en horas, Fase DevOps y Fecha límite. Los cambios de código se integran mediante Pull Requests con revisión de al menos otro integrante.

## Calendario

| Fecha | Actividades |
| --- | --- |
| 22 de noviembre | Creación del repositorio, tablero, historias, issues, estructura inicial y workflow de integración continua. |
| 23 de noviembre | Desarrollo de la interfaz, registro de tareas y consulta del listado. |
| 24 de noviembre | Edición, eliminación, cambio de estado y prioridad; pruebas funcionales y corrección de fallas. |
| 25 de noviembre | Integración final, Release v1.0.0, despliegue en Railway, monitoreo y documentación de entrega. |
| 26 de noviembre | Revisión presencial de 14:00 a 17:00 horas. |

## Entregables

Repositorio, tablero, historias de usuario, issues atendidos, código fuente, ramas, Pull Requests, workflows de Actions, pruebas unitarias y funcionales, evidencias de ejecución, Release v1.0.0, URL pública y documento de resultados.
