# Monitoreo

El workflow `.github/workflows/monitoreo.yml` se denomina `Monitoreo` y se ejecuta de dos formas:

- Programada: cron `0 */6 * * *`, es decir, cada seis horas en hora UTC.
- Manual: `workflow_dispatch`, disponible en Actions.

La frecuencia original era horaria y se cambió a seis horas en el Pull Request #34 para cuidar el crédito del plan Free. La ejecución manual se conservó.

El workflow toma la URL de la variable de repositorio `URL_PUBLICA`, configurada con `https://taskmanager-production-143c7d8d.up.railway.app`, le quita la barra final si la tiene y consulta `/health` y `/` con `curl`. Registra fecha, ruta, código HTTP y tiempo de respuesta; falla si alguna ruta devuelve un código fuera de 2xx/3xx.

## Ejecuciones reales

| Run | Origen | Resultado | Observación |
| --- | --- | --- | --- |
| [45057295341](https://github.com/netfoor/TaskManager-DevOps/actions/runs/45057295341) | Manual desde `main` | Failure | Terminó con código 2 antes de consultar las rutas: el script usaba `for ruta en /health /; do`, sintaxis inválida en Bash. Se registró la incidencia #35. |
| [45057508119](https://github.com/netfoor/TaskManager-DevOps/actions/runs/45057508119) | Manual desde `fix/monitoreo-shell` | Success | `/health` 200 en 1.344063 s; `/` 200 en 0.117429 s. Validó el cambio del PR #36 antes de integrarlo. |
| [45057779144](https://github.com/netfoor/TaskManager-DevOps/actions/runs/45057779144) | Manual final desde `main` | Success | `/health` 200 en 0.053253 s; `/` 200 en 0.039118 s, medidos el 2026-11-22T18:55:22Z. |

La incidencia #35 se corrigió cambiando la sentencia a `for ruta in /health /; do` y se cerró con el Pull Request #36. No se encontraron otras incidencias reales durante el monitoreo posterior al despliegue.

## Evidencia

- `.remedial/evidencias/monitoreo_fallo_45057295341.log`
- `.remedial/evidencias/monitoreo_exitoso_45057508119.txt`
- `.remedial/evidencias/monitoreo_final_main_45057779144.log`
- `.remedial/evidencias/despliegue_verificacion.txt`

El servicio tiene sueño automático habilitado por el plan Free, por lo que la primera petición después de un periodo inactivo puede tardar más; las ejecuciones de monitoreo dejan constancia de esos tiempos.
