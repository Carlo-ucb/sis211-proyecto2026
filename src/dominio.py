# src/dominio.py
# Clases del dominio: Gestión de pedidos de restaurante.
# Aquí NO se implementan cola, lista ni hash. Eso va en estructuras.py por cierto.


class Platillo:
    def __init__(self, codigo, nombre, precio):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = float(precio)

    def __repr__(self):
        return f"Platillo({self.codigo!r}, {self.nombre!r}, {self.precio})"


class Pedido:
    def __init__(self, codigo, cliente, prioridad = 0):
        self.codigo = codigo
        self.cliente = cliente
        self.items = []  # lista de Platillo
        self.estado = "pendiente"
        self.prioridad = prioridad  # v2: menor número = más urgente

    def agregar_item(self, platillo):
        self.items.append(platillo)

    def total(self):
        return sum(item.precio for item in self.items)

    def marcar_listo(self):
        self.estado = "listo"

    def __repr__(self):
        return f"Pedido({self.codigo!r}, {self.cliente!r}, estado={self.estado!r})"