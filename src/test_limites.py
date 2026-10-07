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