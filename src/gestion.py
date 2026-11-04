# src/gestion.py
# Lógica de gestión de pedidos de restaurante.
# v1: Cola (pendientes), Lista (menu/historial), TablaHash (busqueda por codigo).
# v2: Heap (cola de prioridad para atender por urgencia).

from src.dominio import Pedido
from src.estructuras import Cola, Lista, TablaHash, Heap


class GestionPedidos:
    def __init__(self):
        # --- v1 ---
        self.pendientes = Cola()           # familia: cola
        self.historial = Lista()           # familia: lista
        self.menu = Lista()                # familia: lista
        self.indice_pedidos = TablaHash()  # familia: tabla hash
        # --- v2 ---
        self.cola_prioridad = Heap()       # familia: heap

    # --- Menu (v1) ---
    def agregar_platillo_menu(self, platillo):
        self.menu.agregar(platillo)

    def obtener_menu(self):
        return self.menu.todos()

    # --- Pedidos (v1 + v2) ---
    def agregar_pedido(self, pedido):
        if self.indice_pedidos.existe(pedido.codigo):
            raise ValueError(f"Ya existe un pedido con código {pedido.codigo}")
        self.indice_pedidos.insertar(pedido.codigo, pedido)
        self.pendientes.encolar(pedido)                          # v1: FIFO
        self.cola_prioridad.insertar(pedido, pedido.prioridad)   # v2: urgencia

    def atender_siguiente(self):
        """v1: atiende el pedido que llegó primero (FIFO).
        Salta los pedidos que ya fueron atendidos por urgencia."""
        while True:
            pedido = self.pendientes.desencolar()
            if pedido is None:
                return None
            if pedido.estado != "listo":
                pedido.marcar_listo()
                self.historial.agregar(pedido)
                return pedido

    def atender_por_urgencia(self):
        """v2: atiende el pedido más urgente (menor prioridad numérica).
        Si la cola de prioridad está vacía, retorna None."""
        while True:
            pedido = self.cola_prioridad.extraer()
            if pedido is None:
                return None
            if pedido.estado != "listo":
                pedido.marcar_listo()
                self.historial.agregar(pedido)
                return pedido

    def buscar_pedido(self, codigo):
        return self.indice_pedidos.buscar(codigo)

    def obtener_historial(self):
        return self.historial.todos()

    def pedidos_pendientes(self):
        return self.pendientes.tamano()

    # --- v2 ---
    def pedidos_prioritarios(self):
        """Cuántos pedidos hay en la cola de prioridad."""
        return self.cola_prioridad.tamano()

    def proximo_urgente(self):
        """Mira el pedido más urgente sin atenderlo."""
        return self.cola_prioridad.ver_primero()