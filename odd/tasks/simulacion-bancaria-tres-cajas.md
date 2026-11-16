# Simulación bancaria de tres cajas
Implementar un notebook reproducible y comentado para resolver la actividad de teoría de colas del problema bancario.
Modelo principal acordado: tres colas FIFO independientes, una por caja (tres M/M/1 configurables).

## Specs

S1. "revisa los documentos de la actividad, teoria de colas y lo que hay que hacer en la actividad 3 y en el repositorio solucion problema bancario vamos a crear el codigo en ipynb para construir la simulacion de las tre cajas, configurar los tiempos y probabilidades, ejecutar 10 o mas recplicas,validar que el modelo funcione correctamente, y comentar el codigo"

S2. "Tres M/M/1 independientes (recomendado)"

## Tasks

- T1 [S1-S2] route: parent-inline — Consolidar requisitos, supuestos y estructura del notebook. status: done; commit: pending
- T2 [S1-S2] route: parent-inline — Implementar parámetros, motor de simulación y escenarios de tres cajas. status: done; commit: pending
- T3 [S1] route: parent-inline — Ejecutar réplicas y responder los puntos cuantitativos de la actividad. status: in_progress; commit: pending
- T4 [S1] route: parent-inline — Incorporar validaciones, comentarios, interpretación y conclusiones. commit: pending
- T5 [S1-S2] route: independent-verification — Ejecutar el notebook de principio a fin y verificar resultados reproducibles. commit: pending

## Log

L1. "revisa los documentos de la actividad, teoria de colas y lo que hay que hacer en la actividad 3 y en el repositorio solucion problema bancario vamos a crear el codigo en ipynb para construir la simulacion de las tre cajas, configurar los tiempos y probabilidades, ejecutar 10 o mas recplicas,validar que el modelo funcione correctamente, y comentar el codigo"
L2. Decisión registrada mediante selector: "Tres M/M/1 independientes (recomendado)".
L3. Evidencia base revisada: `../S25 - Módulo 2. Actividad didáctica 2-M3.txt`, `../Semana 6 - Teoría de Colas.html`, `../Laboratorio - Problema Bancario.html` y `README.md`.
L4. Supuestos: llegadas hasta el minuto 480 y drenaje posterior; FIFO por caja; en cajas elegibles el cliente elige la menor carga pendiente; criterio de nueva caja documentado dentro del notebook; 30 réplicas por escenario.
