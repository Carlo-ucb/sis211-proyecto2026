# src/estructuras.py
# Estructuras simples para v1.
# Familias: cola, lista, tabla hash.


class Cola:
    """Cola FIFO simple. Familia: cola."""

    def __init__(self):
        self._datos = []

    def encolar(self, item):
        self._datos.append(item)

    def desencolar(self):
        if self.esta_vacia():
            return None
        return self._datos.pop(0)

    def frente(self):
        if self.esta_vacia():
            return None
        return self._datos[0]

    def esta_vacia(self):
        return len(self._datos) == 0

    def tamano(self):
        return len(self._datos)

    def __len__(self):
        return len(self._datos)


class Lista:
    """Lista ordenada simple. Familia: lista."""

    def __init__(self):
        self._datos = []

    def agregar(self, item):
        self._datos.append(item)

    def obtener(self, indice):
        if 0 <= indice < len(self._datos):
            return self._datos[indice]
        return None

    def todos(self):
        return list(self._datos)

    def esta_vacia(self):
        return len(self._datos) == 0

    def tamano(self):
        return len(self._datos)

    def __len__(self):
        return len(self._datos)

    def __iter__(self):
        return iter(self._datos)


class TablaHash:
    """Tabla hash simple (clave -> valor). Familia: hash."""

    def __init__(self):
        self._datos = {}

    def insertar(self, clave, valor):
        self._datos[clave] = valor

    def buscar(self, clave):
        return self._datos.get(clave)

    def eliminar(self, clave):
        if clave in self._datos:
            del self._datos[clave]
            return True
        return False

    def existe(self, clave):
        return clave in self._datos

    def tamano(self):
        return len(self._datos)

    def __len__(self):
        return len(self._datos)