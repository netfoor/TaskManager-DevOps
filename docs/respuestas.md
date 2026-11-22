# Preguntas de análisis

## 1. ¿Qué ventajas ofrece utilizar GitHub Projects para organizar un proyecto de software?

GitHub Projects permite ver el avance del trabajo en un tablero, relacionar cada issue con una tarea concreta y mantener en un solo lugar responsables, prioridades, estimaciones y fechas. En este proyecto sirvió para pasar las historias y tareas de la planeación a columnas como To Do, In Progress y Done, de modo que el estado del equipo es visible sin preguntar uno por uno.

## 2. ¿Cuál es la diferencia entre Git y GitHub?

Git es el sistema de control de versiones que guarda el historial de cambios en el propio repositorio y permite trabajar con ramas, fusiones y revertir versiones. GitHub es una plataforma que aloja esos repositorios y agrega colaboración: Pull Requests, revisión de código, issues, Actions, Releases y Projects.

## 3. ¿Por qué es importante utilizar ramas durante el desarrollo?

Las ramas separan el trabajo en curso del código estable de `main`, para que una funcionalidad incompleta no impida que los demás avancen. Aquí cada requerimiento se desarrolló en una rama propia y llegó a `main` solo después de pasar las pruebas y la revisión.

## 4. ¿Qué función cumple un Pull Request?

Un Pull Request reúne los cambios de una rama, muestra la diferencia respecto a `main`, permite comentar y revisar el código antes de integrarlo, y deja evidencia de quién propuso y quién aprobó el cambio. Además dispara la integración continua para verificar que las pruebas sigan pasando.

## 5. ¿Qué problemas permite detectar la integración continua?

La integración continua detecta pruebas fallidas, dependencias que no se instalan, cambios que rompen funcionalidades existentes y configuraciones de construcción inconsistentes. En este proyecto detectó un error real de ordenamiento del listado: la prueba esperaba la tarea más reciente primero y la aplicación la mostraba al último.

## 6. ¿Cuál es la diferencia entre integración continua y entrega continua?

La integración continua verifica cada cambio automáticamente al fusionarlo, principalmente con construcción y pruebas. La entrega continua agrega la preparación de una versión desplegable: al publicar `v1.0.0`, el workflow genera un artefacto con el código listo para distribuir.

## 7. ¿Qué diferencia existe entre entrega continua y despliegue continuo?

La entrega continua deja un paquete o artefacto listo, pero una persona decide cuándo publicarlo. El despliegue continuo publica automáticamente cada versión aprobada en el entorno de producción; aquí Railway despliega desde `main`, mientras que el artefacto de GitHub se genera al publicar el Release.

## 8. ¿Por qué es importante automatizar las pruebas?

Las pruebas automáticas se ejecutan igual cada vez, sin depender de que alguien recuerde revisar todo a mano. Permiten detectar regresiones en minutos y dan confianza para integrar cambios de varias ramas; en este caso pasaron de 25 a 26 pruebas al agregar la corrección del error de edición.

## 9. ¿Qué sucede si se integra código que contiene errores?

El error llega al resto del equipo y puede afectar otras funcionalidades o la versión publicada. Por eso se usan Pull Requests, integración continua y revisión: el error del ordenamiento se detectó en Actions antes de continuar y la edición de tareas inexistentes se corrigió con un issue, una rama y un PR.

## 10. ¿Por qué DevOps requiere monitorear una aplicación después de publicarla?

Publicar no garantiza que la aplicación siga respondiendo: pueden fallar la base de datos, el servidor, el volumen o una dependencia externa. El monitoreo consulta `/health` y la página principal cada hora y de forma manual, registra códigos y tiempos de respuesta, y falla si el servicio deja de responder.

## 11. ¿Qué beneficios obtiene una empresa al implementar DevOps?

DevOps reduce el tiempo entre el cambio y su entrega, hace repetibles las pruebas y los despliegues, y mejora la trazabilidad de lo que se publicó. También facilita detectar y corregir incidentes con evidencia, en vez de depender de decisiones informales o de una sola persona.

## 12. ¿Cómo podrían mejorar el proceso de desarrollo en una segunda versión?

Para la versión `v1.1.0` se propone agregar autenticación para separar las tareas por usuario, filtros por estado y prioridad para consultar mejor el listado, y notificaciones cuando una tarea cambie de estado. Estas mejoras están registradas como issues con etiqueta `mejora` y agrupadas en un milestone.
