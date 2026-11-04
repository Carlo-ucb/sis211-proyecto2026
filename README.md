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

---


# SIS-211 · Proyecto v1 — Gestión de Pedidos de Restaurante

> **Sistema de gestión de pedidos de restaurante desarrollado para la asignatura SIS-211.**

---

## Información del proyecto

| Campo                 | Información                                                                      |
| --------------------- | -------------------------------------------------------------------------------- |
| **Estudiante**        | Carlo Gennaro Barroso Benavides                                                  |
| **Dominio**           | Gestión de pedidos de restaurante                                                |
| **Repositorio**       | [GitHub — sis211-proyecto2026](https://github.com/Carlo-ucb/sis211-proyecto2026) |
| **Entrega Moodle v1** | `2026-10-07 23:59`                                                               |
| **Branch**            | `v1`                                                                             |
| **Versión**           | `v1`                                                                             |

> **Importante:** Para esta entrega se trabaja únicamente con la branch `v1`. No crear las branches `v2` ni `v3` todavía.

---

## 📋 Descripción

Este proyecto implementa un **software de gestión de pedidos de restaurante**, diseñado para administrar el menú, registrar pedidos y controlar su atención utilizando estructuras de datos simples.

El sistema permite:

* Registrar platillos en el menú.
* Tomar pedidos de clientes.
* Atender los pedidos respetando el orden de llegada (**FIFO**).
* Buscar pedidos mediante su número o código.
* Consultar el historial de pedidos atendidos.

### 🧩 Estructuras de datos utilizadas

La versión `v1` utiliza **tres familias de estructuras simples**, cada una asociada a una necesidad específica del dominio:

| Flujo del dominio              | Estructura     | Implementación                     |
| ------------------------------ | -------------- | ---------------------------------- |
| Siguiente pedido a preparar | **Cola**       | `src/estructuras.py` → `Cola`      |
| Menú e historial del día    | **Lista**      | `src/estructuras.py` → `Lista`     |
| Buscar pedido por número    | **Tabla Hash** | `src/estructuras.py` → `TablaHash` |

>  **No se utilizan árboles ni grafos en la versión `v1`.**

---

## 📁 Estructura del proyecto

```text
sis211-proyecto2026/
│
├── README.md
│
├── src/
│   ├── __init__.py
│   ├── dominio.py          # Clases Platillo y Pedido
│   ├── estructuras.py      # Cola, Lista y TablaHash
│   └── gestion.py          # Lógica de gestión de pedidos
│
└── tests/
    └── test_limites.py     # Pruebas de casos límite
```

### 🔍 Descripción de los archivos

* **`src/dominio.py`**

  * Contiene las clases principales del dominio:

    * `Platillo`
    * `Pedido`

* **`src/estructuras.py`**

  * Implementa las estructuras de datos utilizadas por el sistema:

    * `Cola`
    * `Lista`
    * `TablaHash`

* **`src/gestion.py`**

  * Contiene la lógica principal para administrar:

    * Menú
    * Pedidos
    * Atención de pedidos
    * Historial
    * Búsqueda por código

* **`tests/test_limites.py`**

  * Contiene pruebas para validar el comportamiento del sistema frente a casos límite.

---

# ⚙️ Requisitos

Para ejecutar el proyecto necesitas:

* **Python 3.11 o superior**
* **pytest**

Puedes verificar la versión instalada de Python con:

```bash
python --version
```

Deberías obtener una salida similar a:

```text
Python 3.11.x
```

---

# Instalación

## 1. Clonar el repositorio

Si todavía no tienes el proyecto localmente:

```bash
git clone https://github.com/Carlo-ucb/sis211-proyecto2026.git
cd sis211-proyecto2026
```

---

## 2. Cambiar a la branch `v1`

Asegúrate de trabajar sobre la versión correspondiente a esta entrega:

```bash
git checkout v1
```

Puedes comprobar la branch actual con:

```bash
git branch
```

Deberías ver:

```text
* v1
```

---

## 3. Crear un entorno virtual

Este paso es opcional, pero recomendado.

### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

### macOS / Linux

```bash
python -m venv .venv
source .venv/bin/activate
```

---

## 4. Instalar `pytest`

```bash
pip install pytest
```

---

# 🧪 Ejecutar las pruebas

Desde la raíz del proyecto:

```bash
python -m pytest -q
```

Si todas las pruebas funcionan correctamente, deberías obtener una salida similar a:

```text
3 passed in 0.02s
```

> ℹ️ El tiempo exacto puede variar dependiendo del equipo.

---

## ✅ Pruebas implementadas

Las pruebas cubren los siguientes casos límite:

| Caso                             | Comportamiento esperado |
| -------------------------------- | ----------------------- |
| Atender una cola vacía        | Retorna `None`          |
| Buscar un pedido inexistente  | Retorna `None`          |
| Registrar un pedido duplicado | Lanza `ValueError`      |

Estas pruebas permiten comprobar que el sistema maneja correctamente situaciones que podrían provocar errores durante su utilización.

---

# 💻 Ejemplo de uso

El sistema puede probarse directamente desde la consola interactiva de Python.

Inicia Python:

```bash
python
```

Luego ejecuta:

```python
from src.dominio import Platillo, Pedido
from src.gestion import GestionPedidos

# Crear la gestión de pedidos
g = GestionPedidos()

# Agregar platillos al menú
g.agregar_platillo_menu(
    Platillo(1, "Milanesa", 35.0)
)

g.agregar_platillo_menu(
    Platillo(2, "Ensalada", 20.0)
)

# Crear un pedido
p = Pedido(100, "Ana")

# Agregar productos al pedido
p.agregar_item(
    Platillo(1, "Milanesa", 35.0)
)

p.agregar_item(
    Platillo(2, "Ensalada", 20.0)
)

# Registrar el pedido
g.agregar_pedido(p)

# Buscar pedido por número
print(g.buscar_pedido(100))
# Pedido(100, 'Ana', estado='pendiente')

# Atender el siguiente pedido (FIFO)
atendido = g.atender_siguiente()

print(atendido)
# Pedido(100, 'Ana', estado='listo')

# Ver historial de pedidos atendidos
print(g.obtener_historial())
# [Pedido(100, 'Ana', estado='listo')]

# Intentar atender cuando no hay pedidos pendientes
print(g.atender_siguiente())
# None
```

Para salir del intérprete de Python:

```python
exit()
```

---

# 🔄 Flujo de funcionamiento

El sistema sigue un flujo sencillo para administrar los pedidos:

```text
             ┌─────────────────┐
             │      Menú       │
             │     Lista       │
             └────────┬────────┘
                      │
                      ▼
             ┌─────────────────┐
             │ Crear pedido    │
             │     Pedido      │
             └────────┬────────┘
                      │
                      ▼
             ┌─────────────────┐
             │ Registrar       │
             │ pedido          │
             └────────┬────────┘
                      │
                      ▼
             ┌─────────────────┐
             │      Cola       │
             │      FIFO       │
             └────────┬────────┘
                      │
                      ▼
             ┌─────────────────┐
             │ Atender pedido  │
             └────────┬────────┘
                      │
                      ▼
             ┌─────────────────┐
             │    Historial    │
             │     Lista       │
             └─────────────────┘

        Tabla Hash
        └── Buscar pedido por código
```

---

# 📦 Caso límite implementado

El archivo:

```text
tests/test_limites.py
```

verifica que el sistema maneje correctamente diferentes situaciones límite.

### 1. Cola vacía

Cuando no existen pedidos pendientes y se intenta atender uno:

```python
g.atender_siguiente()
```

El sistema no genera un error y retorna:

```python
None
```

---

### 2. Pedido inexistente

Cuando se busca un pedido cuyo código no está registrado:

```python
g.buscar_pedido(999)
```

El sistema retorna:

```python
None
```

---

### 3. Pedido duplicado

Cuando se intenta registrar dos pedidos utilizando el mismo código:

```python
g.agregar_pedido(pedido)
```

El sistema lanza:

```python
ValueError
```

Esto evita que existan pedidos duplicados dentro del sistema.

---

## 🎯 Cumplimiento de la consigna v1

La implementación cumple con el requisito de probar al menos un **caso límite**, incluyendo:

* ✅ Estructura vacía.
* ✅ Elemento no encontrado.
* ✅ Elemento duplicado.

Además, cada estructura se utiliza de acuerdo con el flujo correspondiente del dominio:

* ✅ **Cola** → atención FIFO.
* ✅ **Lista** → menú e historial.
* ✅ **Tabla Hash** → búsqueda de pedidos por código.

---

---

# SIS-211 · Proyecto v2 — Gestión de Pedidos de Restaurante

> **Misma software que v1. Branch `v2` desde `v1`. Se agrega una jerarquía: heap.**

---

## Información de v2

| Campo | Información |
| --- | --- |
| **Dominio** | Gestión de pedidos de restaurante (el mismo de v1) |
| **Repositorio** | [GitHub — sis211-proyecto2026](https://github.com/Carlo-ucb/sis211-proyecto2026) |
| **Branch** | `v2` (creada desde `v1`) |
| **Entrega Moodle v2** | `2026-11-04 23:59` |
| **Versión** | `v2` |

---

## Flujo nuevo (v2)

**El pedido que la cocina debe sacar ahora, por urgencia, no por orden de llegada.**

En v1, la cocina atendía con una cola FIFO (`atender_siguiente`). Ese flujo no distingue
un pedido urgente (por ejemplo, un cliente con reserva o un plato que se enfría) de uno
común. En v2 se agrega una **cola de prioridad (heap)** para que la cocina pueda extraer
siempre el pedido más urgente, sin importar cuándo llegó.

---

## Familia agregada: heap

| Flujo nuevo | ¿Qué se ordena? | Familia | La uso porque… |
| --- | --- | --- | --- |
| Atender el pedido más urgente | Prioridad (menor número = más urgente) | **Heap** | La cola FIFO de v1 solo respeta el orden de llegada; el heap extrae el mínimo en O(log n) sin recorrer toda la cola. |

> **No se usan árboles ni grafos en v2.** Solo se agrega un heap (cola de prioridad).

---

## Caso límite v2

**Vacío:** si no hay pedidos en la cola de prioridad, `atender_por_urgencia()` retorna `None`
sin lanzar excepción.

```python
def test_atender_por_urgencia_vacio_retorna_none():
    gestion = GestionPedidos()
    assert gestion.atender_por_urgencia() is None