# SIS-211 · Proyecto de curso (2/2026)

Un mismo software que **crece**: v1 (estructuras simples) → v2 (jerárquicas) → v3 (grafos).

**Hoy solo existe la branch `v1`.** No creen `v2` ni `v3`.

| | |
| --- | --- |
| **Estudiante** | Carlo Gennaro Barroso Benavides |
| **Dominio** | Gestión de pedidos de restaurante |
| **Repo** | https://github.com/Carlo-ucb/sis211-proyecto2026 |

## Mapa v1 (mínimo tres familias distintas)

Familias: arreglo, lista, pila, cola, tabla hash.  
`dict` y `set` son **la misma** familia (hash). Sin árboles ni grafos en v1.

| Flujo del dominio | Qué llega / sale / se busca | Familia | La uso porque… |
| --- | --- | --- | --- |
| El siguiente pedido a preparar | Atender pedidos en orden estricto de llegada (FIFO) | Cola | Garantiza que el primer pedido recibido sea el primero en cocinarse. |
| El menú o historial del día | Lista de platillos disponibles e historial ordenado | Lista | Permite almacenar elementos en orden secuencial e iterar sobre ellos. |
| Buscar un pedido por número | Búsqueda directa del estado de un pedido por ID | Tabla Hash | Permite acceso y búsqueda rápida en tiempo promedio constante $O(1)$. |

Cómo probar un caso límite (vacío, no encontrado o duplicado):

> Se verificará que al intentar atender un pedido en una cola vacía no se generen errores inesperados, retornando un mensaje adecuado o valor nulo.

## Carpetas

- `src/` — clases del dominio (POO). Hoy no codeen.
- `tests/` — un caso límite, cuando implementen.

## Alcance

- v1: clases en `.py` (POO). Entrega Moodle: **2026-10-07 23:59**.
- Este README **no** sustituye la tarea de Moodle.
- v2 y v3: otras branches, más adelante, a partir de `v1`.