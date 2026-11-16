# Simulación bancaria de tres cajas
Implementar un notebook reproducible y comentado para resolver la actividad de teoría de colas del problema bancario.
Modelo principal acordado: tres colas FIFO independientes, una por caja (tres M/M/1 configurables).
Delivery strategy: single-pr con dos work-unit commits; slice 1 `d8f1092` (modelo + pruebas, 491 líneas por sobrecosto del JSON del notebook), slice 2 resultados + validación + cierre.

## Specs

S1. "revisa los documentos de la actividad, teoria de colas y lo que hay que hacer en la actividad 3 y en el repositorio solucion problema bancario vamos a crear el codigo en ipynb para construir la simulacion de las tre cajas, configurar los tiempos y probabilidades, ejecutar 10 o mas recplicas,validar que el modelo funcione correctamente, y comentar el codigo"

S2. "Tres M/M/1 independientes (recomendado)"

## Tasks

- T1 [S1-S2] route: parent-inline — Consolidar requisitos, supuestos y estructura del notebook. status: done; commit: pending
- T2 [S1-S2] route: parent-inline — Implementar parámetros, motor de simulación y escenarios de tres cajas. status: done; commit: d8f1092
- T3 [S1] route: parent-inline — Ejecutar réplicas y responder los puntos cuantitativos de la actividad. status: done; commit: pending
- T4 [S1] route: parent-inline — Incorporar validaciones, comentarios, interpretación y conclusiones. status: done; commit: pending
- T5 [S1-S2] route: self-verification — Ejecutar el notebook de principio a fin y verificar resultados reproducibles. status: done; commit: pending

## Log

L1. "revisa los documentos de la actividad, teoria de colas y lo que hay que hacer en la actividad 3 y en el repositorio solucion problema bancario vamos a crear el codigo en ipynb para construir la simulacion de las tre cajas, configurar los tiempos y probabilidades, ejecutar 10 o mas recplicas,validar que el modelo funcione correctamente, y comentar el codigo"
L2. Decisión registrada mediante selector: "Tres M/M/1 independientes (recomendado)".
L3. Evidencia base revisada: `../S25 - Módulo 2. Actividad didáctica 2-M3.txt`, `../Semana 6 - Teoría de Colas.html`, `../Laboratorio - Problema Bancario.html` y `README.md`.
L4. Supuestos: llegadas hasta el minuto 480 y drenaje posterior; FIFO por caja; en cajas elegibles el cliente elige la menor carga pendiente; criterio de nueva caja documentado dentro del notebook; 30 réplicas por escenario.
L5. Resultados baseline: espera media 0.472 min, p95 3.363 min; no se recomienda cuarta caja bajo los umbrales documentados. Si se exige exclusividad, una caja para retiros y dos para pagos obtiene la menor espera entre las dos alternativas exclusivas.
L6. Verificación: 11/11 celdas ejecutadas, 0 errores, 4/4 pruebas unitarias aprobadas. El verificador independiente no alcanzó a ejecutar pruebas por una ruta de workspace incorrecta; `gentle_review assess` confirmó que, sin escalamiento de riesgo alto, corresponde self-verification y no un segundo intento del verificador.
