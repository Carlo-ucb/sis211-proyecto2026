# src/estructuras.py
# Estructuras simples para v1.
# Familias: cola, lista, tabla hash.
# v1: cola, lista, tabla hash.
# v2: se agrega heap (cola de prioridad).


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

class Heap:

    def __init__(self):
        self._datos = []  # lista de tuplas (prioridad, item)

    def insertar(self, item, prioridad):
        """Inserta un item con su prioridad."""
        self._datos.append((prioridad, item))
        self._flotar(len(self._datos) - 1)

    def extraer(self):
        """Extrae el item con menor prioridad. None si está vacío."""
        if not self._datos:
            return None
        if len(self._datos) == 1:
            return self._datos.pop()[1]
        # Mover raíz al final y sacarla
        self._datos[0], self._datos[-1] = self._datos[-1], self._datos[0]
        _, item = self._datos.pop()
        self._hundir(0)
        return item

    def ver_primero(self):
        """Devuelve el item más urgente sin extraerlo."""
        if not self._datos:
            return None
        return self._datos[0][1]

    def esta_vacio(self):
        return len(self._datos) == 0

    def tamano(self):
        return len(self._datos)

    def _flotar(self, i):
        """Sube el elemento en la posición i hasta donde corresponda."""
        while i > 0:
            padre = (i - 1) // 2
            if self._datos[i][0] < self._datos[padre][0]:
                self._datos[i], self._datos[padre] = self._datos[padre], self._datos[i]
                i = padre
            else:
                break

    def _hundir(self, i):
        """Baja el elemento en la posición i hasta donde corresponda."""
        n = len(self._datos)
        while True:
            izq = 2 * i + 1
            der = 2 * i + 2
            menor = i
            if izq < n and self._datos[izq][0] < self._datos[menor][0]:
                menor = izq
            if der < n and self._datos[der][0] < self._datos[menor][0]:
                menor = der
            if menor == i:
                break
            self._datos[i], self._datos[menor] = self._datos[menor], self._datos[i]
            i = menor