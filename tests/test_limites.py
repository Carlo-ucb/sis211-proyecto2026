# Un caso límite (vacío, no encontrado o duplicado).
# Completen el lunes 14; hoy solo el README.


# tests/test_limites.py
import pytest

from src.dominio import Pedido
from src.gestion import GestionPedidos


def test_atender_cola_vacia_retorna_none():
    gestion = GestionPedidos()
    assert gestion.atender_siguiente() is None


def test_buscar_pedido_inexistente_retorna_none():
    gestion = GestionPedidos()
    assert gestion.buscar_pedido(999) is None


def test_no_permite_pedido_duplicado():
    gestion = GestionPedidos()
    pedido = Pedido(1, "Ana")
    gestion.agregar_pedido(pedido)

    with pytest.raises(ValueError):
        gestion.agregar_pedido(Pedido(1, "Luis"))

# --- v2: heap / urgencia ---

def test_atender_por_urgencia_vacio_retorna_none():
    """Caso límite v2: no hay pedidos en la cola de prioridad."""
    gestion = GestionPedidos()
    assert gestion.atender_por_urgencia() is None


def test_atender_por_urgencia_extrae_el_mas_urgente():
    """v2: prioridad 1 sale antes que prioridad 5."""
    gestion = GestionPedidos()
    gestion.agregar_pedido(Pedido(1, "Ana", prioridad=5))
    gestion.agregar_pedido(Pedido(2, "Luis", prioridad=1))
    gestion.agregar_pedido(Pedido(3, "Eva", prioridad=3))

    urgente = gestion.atender_por_urgencia()
    assert urgente.codigo == 2  # prioridad 1

    siguiente = gestion.atender_por_urgencia()
    assert siguiente.codigo == 3  # prioridad 3

    ultimo = gestion.atender_por_urgencia()
    assert ultimo.codigo == 1  # prioridad 5