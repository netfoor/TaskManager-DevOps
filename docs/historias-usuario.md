# Historias de usuario

Las historias se derivan de los requerimientos funcionales RF01 a RF06 del enunciado. Cada historia queda registrada como un issue en el repositorio y en el tablero del proyecto.

## HU01 Registrar tareas (RF01)

Como usuario del sistema, quiero registrar nuevas tareas para organizar mis actividades y evitar perder información.

Criterios de aceptación:

- El sistema permite ingresar el nombre de la tarea.
- El sistema permite agregar una descripción.
- El sistema permite seleccionar una prioridad Alta, Media o Baja.
- El sistema guarda la tarea y muestra un mensaje de confirmación.

Issue: https://github.com/netfoor/TaskManager-DevOps/issues/1

## HU02 Consultar tareas (RF02)

Como usuario del sistema, quiero consultar todas las tareas registradas para conocer el trabajo pendiente y avanzado.

Criterios de aceptación:

- El sistema muestra el listado de tareas en la página principal.
- El listado incluye nombre, descripción, estado y prioridad.
- Si no hay tareas, el sistema muestra un mensaje informativo.

Issue: https://github.com/netfoor/TaskManager-DevOps/issues/2

## HU03 Editar tareas (RF03)

Como usuario del sistema, quiero editar una tarea existente para corregir o actualizar su información.

Criterios de aceptación:

- El sistema permite modificar nombre, descripción y prioridad.
- El sistema conserva el estado actual de la tarea.
- El sistema muestra un mensaje de confirmación al guardar.

Issue: https://github.com/netfoor/TaskManager-DevOps/issues/3

## HU04 Eliminar tareas (RF04)

Como usuario del sistema, quiero eliminar tareas que ya no son necesarias para mantener el listado limpio y evitar duplicidad.

Criterios de aceptación:

- El sistema solicita confirmación antes de eliminar.
- El sistema elimina la tarea de la base de datos.
- La tarea desaparece del listado y se muestra un mensaje de confirmación.

Issue: https://github.com/netfoor/TaskManager-DevOps/issues/4

## HU05 Cambiar estado de tareas (RF05)

Como usuario del sistema, quiero cambiar el estado de una tarea para dar seguimiento a su progreso.

Criterios de aceptación:

- El sistema permite seleccionar Pendiente, En proceso o Terminada.
- El cambio se guarda y se refleja en el listado.
- El sistema muestra un mensaje de confirmación.

Issue: https://github.com/netfoor/TaskManager-DevOps/issues/5

## HU06 Asignar prioridad a tareas (RF06)

Como usuario del sistema, quiero asignar una prioridad a cada tarea para identificar qué actividades requieren atención primero.

Criterios de aceptación:

- El sistema permite seleccionar Alta, Media o Baja.
- La prioridad se guarda y se refleja en el listado.
- El sistema valida que la prioridad sea una de las opciones permitidas.

Issue: https://github.com/netfoor/TaskManager-DevOps/issues/6
