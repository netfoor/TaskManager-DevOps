# Despliegue en Railway

La aplicación se publicó el 22 de noviembre de 2026 en Railway. Se reutilizó el proyecto existente `adequate-harmony`; no se creó un proyecto nuevo porque el workspace tiene plan Free.

| Dato | Valor |
| --- | --- |
| Proyecto | `adequate-harmony` |
| ID del proyecto | `b3eacd4f-f227-4133-81bb-a0609c55d9a4` |
| Entorno | `production` (`560b635d-9b69-46b8-a39e-6c368e3d8cd2`) |
| Servicio | `taskmanager` (`9ef76173-172a-4d44-ac75-5928a4f0f902`) |
| Repositorio conectado | `netfoor/TaskManager-DevOps@main` |
| Volumen | `taskmanager-data`, 100 MB, montado en `/data` |
| Base de datos | `/data/tareas.db` |
| Dominio público | https://taskmanager-production-143c7d8d.up.railway.app |
| Comando de inicio | `gunicorn app:app --bind 0.0.0.0:$PORT --workers 1` |
| Región del despliegue activo | `iad` |
| Despliegue activo | `241faf30-7bfc-4512-80f2-db778359a367`, commit `1436fde`, SUCCESS |
| Modo de sueño | Habilitado, requisito del plan Free |

Las variables configuradas son `TASKMANAGER_DB=/data/tareas.db` y `TASKMANAGER_SECRET_KEY` con un valor secreto generado al azar. El valor del secreto no se guarda en este repositorio. Railway aporta `PORT` y sus variables de entorno estándar.

Para enlazar el contexto sin afectar otros servicios:

```sh
railway link --project b3eacd4f-f227-4133-81bb-a0609c55d9a4 \
  --environment production \
  --service 9ef76173-172a-4d44-ac75-5928a4f0f902
```

El servicio existente `semiconductores` no fue modificado, reiniciado ni tuvo cambios en sus variables.

## Verificación

- La página principal respondió código 200 en la URL pública.
- `/health` devolvió `{"base_de_datos":"disponible","estado":"ok","ruta":"/data/tareas.db"}` con código 200.
- Se verificaron en producción el registro, la edición, el cambio de estado, el cambio de prioridad y la eliminación de una tarea; la tarea de prueba se eliminó al final.
- La salida completa está en `.remedial/evidencias/despliegue_verificacion.txt`.

Los despliegues posteriores `15229257-fe5a-4570-9305-c8054f1a2757` y `b4cc61a3-5b8d-4865-96b3-29e433d5b8fe` quedaron en `NEEDS_APPROVAL` porque solo cambiaban workflows de GitHub y no el código de la aplicación. La instancia activa sigue siendo el despliegue verificado `241faf30-7bfc-4512-80f2-db778359a367`; esos dos pendientes requieren aprobación manual en Railway si se desea dejar el panel sin despliegues en espera.
