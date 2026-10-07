# src/gestion.py
# Aqui va la logica de gestion de pedidos de restaurante.
# Usa: Cola (pendientes), Lista (menu/historial), TablaHash (busqueda por codigo).

from src.dominio import Pedido
from src.estructuras import Cola, Lista, TablaHash


class GestionPedidos:
    def __init__(self):
        self.pendientes = Cola()           # familia: cola
        self.historial = Lista()           # familia: lista
        self.menu = Lista()                # familia: lista
        self.indice_pedidos = TablaHash()  # familia: tabla hash

    # --- Menú ---
    def agregar_platillo_menu(self, platillo):
        self.menu.agregar(platillo)

    def obtener_menu(self):
        return self.menu.todos()

    # --- Pedidos ---
    def agregar_pedido(self, pedido):
        if self.indice_pedidos.existe(pedido.codigo):
            raise ValueError(f"Ya existe un pedido con código {pedido.codigo}")
        self.indice_pedidos.insertar(pedido.codigo, pedido)
        self.pendientes.encolar(pedido)

    def atender_siguiente(self):
        pedido = self.pendientes.desencolar()
        if pedido is None:
            return None
        pedido.marcar_listo()
        self.historial.agregar(pedido)
        return pedido

    def buscar_pedido(self, codigo):
        return self.indice_pedidos.buscar(codigo)

    def obtener_historial(self):
        return self.historial.todos()

    def pedidos_pendientes(self):
        return self.pendientes.tamano()