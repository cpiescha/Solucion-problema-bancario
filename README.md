# Simulacion del Problema Bancario — Teoria de Colas

Simulacion por eventos discretos del sistema de colas de un banco con tres cajeros independientes (modelo M/M/1). El objetivo es evaluar el desempeno actual, determinar si se necesita un cuarto cajero y comparar distribuciones exclusivas de cajas para pagos y retiros.

## Contexto del problema

El Banco de Colombia opera 8 horas diarias con tres cajas que atienden retiros (70 % de los usuarios) y pagos/consignaciones (30 %). Cada cajero funciona como un sistema M/M/1 independiente. Los tiempos de llegada y servicio siguen distribuciones exponenciales cuyos parametros dependen del tipo de accion y del tipo de usuario (rapido, normal, lento, muy lento).

La actividad pide:

1. Identificar el cajero con menor y mayor tiempo promedio de atencion.
2. Calcular el promedio de usuarios de cada tipo en la totalidad de cajeros.
3. Determinar el total de usuarios por tipo en cada replica y la replica con menor cantidad.
4. Definir si es necesario crear un nuevo cajero usando tiempos de espera.
5. Decidir cuantos cajeros deben ser exclusivos para pagos y cuantos para retiros.

## Estructura del repositorio

```
Solucion-problema-bancario/
├── simulacion_bancaria_tres_cajas.ipynb   # Notebook principal con simulacion, graficas y resultados
├── README.md                              # Este archivo
├── scripts/
│   └── execute_notebook.py                # Script para ejecutar el notebook desde terminal
└── tests/
    └── test_notebook_model.py             # Pruebas unitarias del modelo
```

## Requisitos

- Python 3.10 o superior
- Paquetes: `numpy`, `pandas`, `matplotlib`

Instalacion rapida:

```bash
pip install numpy pandas matplotlib
```

## Como ejecutar

### Opcion 1 — Jupyter Notebook (recomendado)

```bash
cd Solucion-problema-bancario
jupyter notebook simulacion_bancaria_tres_cajas.ipynb
```

Ejecutar todas las celdas en orden y guardar el notebook. Todos los resultados, tablas y graficas quedan embebidos en las salidas del propio notebook. No se generan archivos externos.

### Opcion 2 — Desde terminal

```bash
cd Solucion-problema-bancario
python scripts/execute_notebook.py
```

El script guarda stdout/stderr y las dos graficas como outputs Jupyter `display_data` con PNG en base64 dentro del notebook. Cierra las figuras tras cada celda; no requiere Jupyter para ejecutar.

### Opcion 3 — Pruebas unitarias

```bash
cd Solucion-problema-bancario
python -m unittest tests.test_notebook_model -v
```

## Escenarios simulados

| Escenario | Descripcion |
|-----------|-------------|
| `tres_mixtas` | 3 cajas que atienden retiros y pagos (configuracion actual) |
| `una_retiros_dos_pagos` | 1 caja exclusiva para retiros, 2 para pagos |
| `dos_retiros_un_pago` | 2 cajas exclusivas para retiros, 1 para pagos |
| `cuatro_mixtas` | 4 cajas mixtas (evalua necesidad de ampliar) |

Cada escenario se ejecuta con 30 replicas independientes (semillas reproducibles).

## Resultados principales

- Las tres cajas mixtas presentan una espera media de **0.47 min** y un percentil 95 de **3.36 min**.
- **No se recomienda** crear una cuarta caja (la espera esta por debajo de los umbrales definidos).
- Las distribuciones exclusivas empeoran el servicio: la mejor (1 retiro + 2 pagos) tiene una espera media de 4.15 min, casi 9 veces mayor que la configuracion mixta.
- La configuracion actual de tres cajas mixtas es la mas eficiente.

## Validacion

El modelo se valida con:

- Conservacion de clientes (todos los que llegan son atendidos).
- Coherencia temporal (ningun servicio inicia antes de la llegada).
- Elegibilidad de cajas (ningun cliente va a una caja que no atiende su accion).
- Reproducibilidad (misma semilla produce identicos resultados).
- Frecuencias observadas cercanas a las probabilidades teoricas.
- Ley de Little (Lq = lambda * Wq) con error maximo del orden de 10^-16.
