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

    def verificar_camino(self, i_pos, fila_ganar, fila_bloqueo, col_bloqueo):
        fila, col = i_pos
        casilla_original = self.obtener_posicion(fila_bloqueo, col_bloqueo)
        self.cambiar_casilla(fila_bloqueo, col_bloqueo, "⛔")
        if fila == fila_ganar:
            self.cambiar_casilla(fila_bloqueo, col_bloqueo, casilla_original)
            return True
        
        valor_actual = self.obtener_posicion(fila, col)
        self.cambiar_casilla(fila, col, "0")

        direcciones = LinkedList()
        direcciones.add_head((-1,0))
        direcciones.add_head((0,-1))
        direcciones.add_head((1,0))
        direcciones.add_head((0,1))

        current = direcciones.head

        while current:
            temp_fila, temp_col = current.value
            nueva_fila, nueva_col = fila + temp_fila, col + temp_col

            if self.verificar_posicion(nueva_fila, nueva_col):
                if self.obtener_posicion(nueva_fila, nueva_col) != "0":
                    if self.obtener_posicion(nueva_fila, nueva_col) != "⛔":
                        if self.verificar_camino((nueva_fila, nueva_col), fila_ganar, fila_bloqueo, col_bloqueo):
                            self.cambiar_casilla(fila, col, valor_actual)
                            self.cambiar_casilla(fila_bloqueo, col_bloqueo, casilla_original)
                            return True
            current = current.next
                            
        self.cambiar_casilla(fila, col, valor_actual)
        self.cambiar_casilla(fila_bloqueo, col_bloqueo, casilla_original)
        return False
    