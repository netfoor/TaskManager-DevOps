# Pruebas funcionales

Las pruebas se ejecutaron contra la aplicación real en local, con Python 3.13, Flask 3.1.3 y una base SQLite temporal definida con `TASKMANAGER_DB`. La salida completa de la ejecución está en `.remedial/evidencias/funcional_local.txt` y la de las pruebas automáticas en `.remedial/evidencias/pytest_integrado.txt`.

| ID | Prueba y pasos | Resultado esperado | Resultado obtenido | Estado |
| --- | --- | --- | --- | --- |
| CP01 | Registrar una tarea: enviar nombre «Elaborar documentacion», descripción y prioridad Alta desde el formulario. | La tarea se guarda y aparece en el listado con mensaje de confirmación. | Mensaje «La tarea se registró correctamente.» y tarea visible con identificador 1. | Aprobado |
| CP02 | Registrar una tarea sin nombre: dejar el campo nombre con espacios. | El sistema muestra una validación y no guarda. | Mensaje «El nombre de la tarea es obligatorio.»; el total de tareas permanece en 1. | Aprobado |
| CP03 | Consultar tareas: abrir la página principal. | Se muestra el listado de tareas. | Encabezado «Tareas registradas» y la tarea registrada aparecen en la tabla. | Aprobado |
| CP04 | Editar una tarea: cambiar nombre, descripción y prioridad desde el formulario de edición. | Se actualiza la información y se muestra confirmación. | Mensaje «La tarea se actualizó correctamente.» y aparece «Elaborar documentacion final». | Aprobado |
| CP05 | Eliminar una tarea: registrar una temporal y confirmar su eliminación. | La tarea desaparece del listado. | Mensaje «La tarea se eliminó correctamente.»; quedó una sola tarea. | Aprobado |
| CP06 | Cambiar estado: enviar «Terminada» desde el control de estado. | Se actualiza el estado en el listado. | Mensaje de confirmación y etiqueta «Terminada» en la fila. | Aprobado |
| CP07 | Seleccionar prioridad: enviar «Baja» desde el control de prioridad. | Se guarda la prioridad elegida. | Mensaje de confirmación y etiqueta con clase `etiqueta--baja`. | Aprobado |
| CP08 | Editar una tarea inexistente: enviar datos válidos a `/tareas/9999/editar`. | No debe confirmarse una actualización que no ocurrió. | Se mostró «La tarea se actualizó correctamente.» sin existir la tarea. | Fallido, corregido |
| CP09 | Consultar `/health`. | JSON con estado `ok` y base disponible, código 200. | `{"base_de_datos":"disponible","estado":"ok",...}`, código 200 y 0.004 s de respuesta. | Aprobado |

## Error detectado y corrección

El caso CP08 reveló un error real en la edición: la ruta POST no comprobaba que la tarea existiera antes de actualizar, por lo que informaba de un guardado inexistente. Se registró el issue https://github.com/netfoor/TaskManager-DevOps/issues/26 con funcionalidad afectada, pasos para reproducir, resultado obtenido, esperado y prioridad.

La corrección verifica la existencia de la tarea en la petición POST y muestra «No se encontró la tarea solicitada.»; se agregó una prueba de regresión y la ejecución completa quedó en 26 pruebas aprobadas. El cambio se integra mediante el Pull Request de la rama `fix/editar-inexistente`.

## Pruebas automáticas

La integración de las cuatro ramas de funcionalidades ejecutó 25 pruebas unitarias antes de la corrección y 26 después. Todas las pruebas llaman a funciones reales de la aplicación mediante el cliente de pruebas de Flask y una base SQLite temporal.
