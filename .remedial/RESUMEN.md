# Resumen final del remedial

Fecha de cierre: 22 de noviembre de 2026.

## Enlaces principales

- Repositorio: https://github.com/netfoor/TaskManager-DevOps
- Tablero GitHub Projects #2: https://github.com/users/netfoor/projects/2
- Aplicación publicada: https://taskmanager-production-143c7d8d.up.railway.app
- Release v1.0.0: https://github.com/netfoor/TaskManager-DevOps/releases/tag/v1.0.0
- Entrega continua: https://github.com/netfoor/TaskManager-DevOps/actions/runs/45055670829
- Monitoreo final: https://github.com/netfoor/TaskManager-DevOps/actions/runs/45057779144

## Fases completadas

| Fase | Resultado | Evidencia |
| --- | --- | --- |
| 1. Git, GitHub y ramas | Repositorio, 10 Pull Requests integrados, revisión de Israel. | PR #21 a #36. |
| 2. GitHub Projects | 20 issues y 6 historias cargadas con prioridad, estimación, fase y fecha; #12 y #13 eliminados por duplicados. | Proyecto #2 y `.remedial/ids.json`. |
| 3. Integración continua | Falla real detectada y corregida; todas las PRs posteriores pasaron. | Runs 45051866776 y 45051957172; `docs/ci.md`. |
| 4. Funcionalidades | Registro, consulta, edición, eliminación, estado y prioridad implementados. | PR #22 a #25; 26 pruebas. |
| 5. Entrega continua | Release `v1.0.0`, artefacto `TaskManager-v1` generado y verificado. | Run 45055670829; `.remedial/evidencias/entrega_artefacto.txt`. |
| 6. Despliegue | Railway reutilizó `adequate-harmony`, servicio `taskmanager`, volumen de 100 MB y dominio público. | `docs/despliegue.md`; despliegue `241faf30-7bfc-4512-80f2-db778359a367`. |
| 7. Monitoreo y mejoras | Monitoreo cada 6 horas y manual; incidencia real detectada, documentada y corregida; tres mejoras propuestas. | `docs/monitoreo.md`; issues #35, #28, #29 y #30. |

## Issues

- Historias de usuario #1 a #6: todas cerradas. #3, #4, #5 y #6 se cerraron con las implementaciones de las PR #23, #24, #25 y #25 respectivamente.
- Tareas #7 a #11: cerradas. #7 con la PR #21, #9 con la PR #22, #10 con la PR #21 y #22, #11 con la PR #23; #8 se cerró con la interfaz implementada en las PR #21 a #25.
- Tareas #14 a #20: cerradas. #14 con la PR #24, #15 con la PR #25, #16 con la PR #21, #17 con las pruebas funcionales y automáticas, #18 con la PR #32 y el Release, #19 con el despliegue en Railway y #20 con las PR #34 y #36 más el monitoreo final.
- #12 y #13: eliminados por duplicados.
- #26: error real al editar una tarea inexistente; cerrado con la PR #27.
- #28, #29 y #30: mejoras abiertas para `v1.1.0` (autenticación, filtros y notificaciones).
- #31: cerrado; sirve como evidencia de la Fase 3, con etiquetas `bug` y `ci`, no como incidencia operativa.
- #35: incidencia real del monitoreo cerrada con la PR #36.
- Los responsables de las tareas de Luis Joel se indicaron en la descripción de cada issue, sin asignar el campo assignee, según el enunciado.

## Pull Requests

| PR | Rama | Contenido | Estado |
| --- | --- | --- | --- |
| [#21](https://github.com/netfoor/TaskManager-DevOps/pull/21) | `chore/estructura-inicial` | Estructura base, consulta y corrección de orden. | Merged |
| [#22](https://github.com/netfoor/TaskManager-DevOps/pull/22) | `feature/registro-tareas` | RF01, registro de tareas. | Merged |
| [#23](https://github.com/netfoor/TaskManager-DevOps/pull/23) | `feature/editar-tareas` | RF03, edición de tareas. | Merged |
| [#24](https://github.com/netfoor/TaskManager-DevOps/pull/24) | `feature/eliminar-tareas` | RF04, eliminación de tareas. | Merged |
| [#25](https://github.com/netfoor/TaskManager-DevOps/pull/25) | `feature/estado-prioridad` | RF05 y RF06, estado y prioridad. | Merged |
| [#27](https://github.com/netfoor/TaskManager-DevOps/pull/27) | `fix/editar-inexistente` | Corrección del issue #26 y prueba de regresión. | Merged |
| [#32](https://github.com/netfoor/TaskManager-DevOps/pull/32) | `docs/entrega-monitoreo` | Workflows de entrega y monitoreo, respuestas y pruebas. | Merged |
| [#33](https://github.com/netfoor/TaskManager-DevOps/pull/33) | `chore/gunicorn` | Dependencia `gunicorn` para producción. | Merged |
| [#34](https://github.com/netfoor/TaskManager-DevOps/pull/34) | `ci/monitoreo-6h` | Cron de monitoreo cada seis horas. | Merged |
| [#36](https://github.com/netfoor/TaskManager-DevOps/pull/36) | `fix/monitoreo-shell` | Corrección de la incidencia #35. | Merged |

El PR final de documentación y este resumen se entregan en la rama `docs/final`.

## Ejecuciones de Actions

- Integración continua fallida real: [45051866776](https://github.com/netfoor/TaskManager-DevOps/actions/runs/45051866776).
- Integración continua corregida: [45051957172](https://github.com/netfoor/TaskManager-DevOps/actions/runs/45051957172).
- Integración continua de las PRs funcionales: 45052578947, 45052581616, 45052587354 y 45052589214, todas en success.
- Integración continua tras correcciones y dependencias: 45054946943, 45054954056, 45054963764, 45056229980 y 45057501621, todas en success.
- Integración continua en `main` tras integraciones: 45055567240, 45055549702, 45055526563, 45056458896 y 45057709595, todas en success.
- Entrega continua del Release: [45055670829](https://github.com/netfoor/TaskManager-DevOps/actions/runs/45055670829), success.
- Monitoreo fallido real: [45057295341](https://github.com/netfoor/TaskManager-DevOps/actions/runs/45057295341).
- Monitoreo corregido desde rama: [45057508119](https://github.com/netfoor/TaskManager-DevOps/actions/runs/45057508119).
- Monitoreo final desde `main`: [45057779144](https://github.com/netfoor/TaskManager-DevOps/actions/runs/45057779144), con `/health` 200 y `/` 200.

## Release y artefacto

- Tag: `v1.0.0`.
- Release: https://github.com/netfoor/TaskManager-DevOps/releases/tag/v1.0.0.
- Workflow: [45055670829](https://github.com/netfoor/TaskManager-DevOps/actions/runs/45055670829).
- Artefacto: `TaskManager-v1`, id `14767231987`, 7606 bytes.
- Contenido verificado: `app.py`, `requirements.txt`, plantillas y archivos estáticos.
- Evidencia: `.remedial/evidencias/entrega_artefacto.txt`.

## Despliegue

- Proyecto existente: `adequate-harmony` (`b3eacd4f-f227-4133-81bb-a0609c55d9a4`); no se creó uno nuevo.
- Servicio: `taskmanager` (`9ef76173-172a-4d44-ac75-5928a4f0f902`), entorno `production`.
- Volumen único: `taskmanager-data`, 100 MB, montado en `/data`.
- Base de datos: `/data/tareas.db`.
- Dominio: https://taskmanager-production-143c7d8d.up.railway.app.
- Despliegue activo verificado: `241faf30-7bfc-4512-80f2-db778359a367`, commit `1436fde`, región `iad`, SUCCESS.
- Variables: `TASKMANAGER_DB` y `TASKMANAGER_SECRET_KEY`; el secreto no se guarda en el repositorio.
- El servicio `semiconductores` no fue modificado.

## Evidencias

- Funcionales locales: `.remedial/evidencias/funcional_local.txt`.
- Pruebas integradas: `.remedial/evidencias/pytest_integrado.txt` y `.remedial/evidencias/pytest_main_integrado.txt`.
- CI fallido y corregido: `.remedial/evidencias/ci_run_45051866776_fallo.log` y `.remedial/evidencias/pytest_estructura_corregido.txt`.
- Entrega: `.remedial/evidencias/entrega_artefacto.txt`.
- Despliegue: `.remedial/evidencias/despliegue_verificacion.txt`.
- Monitoreo: `.remedial/evidencias/monitoreo_fallo_45057295341.log`, `.remedial/evidencias/monitoreo_exitoso_45057508119.txt` y `.remedial/evidencias/monitoreo_final_main_45057779144.log`.

## Pendientes y limitaciones

- Capturas de pantalla: este worker no tiene herramienta de navegador; la evidencia entregada es de terminal y Actions. El coordinador puede tomar las capturas desde su navegador.
- Los despliegues `15229257-fe5a-4570-9305-c8054f1a2757` y `b4cc61a3-5b8d-4865-96b3-29e433d5b8fe` están en `NEEDS_APPROVAL` en Railway porque solo cambiaban workflows; no afectan a la instancia activa y requieren aprobación manual si se quiere limpiar el panel.
- El servicio tiene sueño automático habilitado por el plan Free; la primera petición tras inactividad puede tardar unos segundos.
- Las mejoras #28, #29 y #30 quedan planificadas para `v1.1.0`, fuera del alcance de esta entrega.
- No se encontraron otras incidencias reales posteriores al despliegue además de #35.
