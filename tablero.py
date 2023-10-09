from linkedlist import LinkedList


class Tablero:
    def __init__(self, tamano):
        self.tamano: int = tamano
        self.tablero = self.crear_tablero()

    def crear_tablero(self):
        tablero = LinkedList()

        for i in range(self.tamano):
            fila = LinkedList()
            for j in range(self.tamano):
                fila.add_head(None)
            tablero.add_head(fila)
        return tablero

    def mostrar_tablero(self):
        fila = self.tablero.head
        while fila:
            current = fila.value.head
            fila_mostrar = ''
            while current:
                fila_mostrar += current.value
                current = current.next
            print(fila_mostrar)
            fila = fila.next

    def celdas(self):
        celdas = ['🔳'] * (self.tamano * self.tamano)

        fila = self.tablero.head
        while fila:
            current = fila.value.head
            while current:
                if celdas and current.value is None:
                    current.value = celdas.pop()
                current = current.next
            fila = fila.next

    def posicion_inicial_x(self):
        fila = self.tamano - 1
        col = (self.tamano // 2)

        if self.verificar_posicion(fila, col):
            self.cambiar_casilla(fila, col, '❌')
            return fila, col

    def posicion_inicial_y(self):
        fila = 0
        col = (self.tamano // 2)

        if self.verificar_posicion(fila, col):
            self.cambiar_casilla(fila, col, '🤖')
            return fila, col

    def verificar_posicion(self, fila: int, col: int):
        validacion: bool = 0 <= fila < self.tamano and 0 <= col < self.tamano
        return validacion

    def obtener_posicion(self, fila, col):
        nodo_fila = self.tablero.head

        for i in range(fila):
            nodo_fila = nodo_fila.next

        current = nodo_fila.value.head
        for i in range(col):
            current = current.next

        return current.value

    def cambiar_casilla(self, fila, col, valor):
        nodo_fila = self.tablero.head

        for i in range(fila):
            nodo_fila = nodo_fila.next

        current = nodo_fila.value.head
        for i in range(col):
            current = current.next

        current.value = valor
