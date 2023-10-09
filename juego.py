from random import randint
from tablero import Tablero


class Juego:
    def __init__(self, tablero: Tablero):
        self.tablero = tablero
        self.pos_x = None
        self.pos_y = None

    def iniciar_x(self):
        self.pos_x = self.tablero.posicion_inicial_x()

    def iniciar_y(self):
        self.pos_y = self.tablero.posicion_inicial_y()

    def saltar_dos_veces(self, fila, col, direccion, pos):
        if direccion == "1":
            fila -= 1
        elif direccion == "2":
            fila += 1
        elif direccion == "3":
            col -= 1
        elif direccion == "4":
            col += 1

        if not self.tablero.verificar_posicion(fila, col):
            print("No te puedes salir de los bordes")
            fila, col = pos

        valor = self.tablero.obtener_posicion(fila, col)
        if valor == '⛔':
            print("La celda está bloqueada")
            fila, col = pos

        return fila, col

    def movimiento_x(self):
        while True:
            direccion = input("Movimiento:\n1: arriba\n2: abajo\n3: izquierda\n4: derecha\n->  ")

            nueva_fila, nueva_col = self.pos_x

            if direccion == "1":
                nueva_fila -= 1
            elif direccion == "2":
                nueva_fila += 1
            elif direccion == "3":
                nueva_col -= 1
            elif direccion == "4":
                nueva_col += 1
            else:
                print('Ingrese 1, 2, 3 o 4')
                continue

            if self.tablero.verificar_posicion(nueva_fila, nueva_col):
                node_value = self.tablero.obtener_posicion(nueva_fila, nueva_col)

                if node_value == '⛔':
                    print("La celda está bloqueada, intente de nuevo")
                    continue

                if node_value == '🤖':
                    fila_salto, col_salto = self.saltar_dos_veces(nueva_fila, nueva_col, direccion, self.pos_x)
                    self.tablero.cambiar_casilla(self.pos_x[0], self.pos_x[1], '🔳')
                    self.pos_x = (fila_salto, col_salto)
                    self.tablero.cambiar_casilla(fila_salto, col_salto, '❌')
                    return

                else:
                    self.tablero.cambiar_casilla(self.pos_x[0], self.pos_x[1], '🔳')
                    self.tablero.cambiar_casilla(nueva_fila, nueva_col, '❌')
                self.pos_x = (nueva_fila, nueva_col)
                return

            else:
                print("No puedes hacer ese movimiento")
                continue

    def movimiento_y(self):
        while True:
            direccion = str(randint(1, 4))
            nueva_fila, nueva_col = self.pos_y

            if direccion == "1":
                nueva_fila -= 1
            elif direccion == "2":
                nueva_fila += 1
            elif direccion == "3":
                nueva_col -= 1
            elif direccion == "4":
                nueva_col += 1
            else:
                continue

            if self.tablero.verificar_posicion(nueva_fila, nueva_col):
                valor_nodo = self.tablero.obtener_posicion(nueva_fila, nueva_col)

                if valor_nodo == '⛔':
                    continue

                if valor_nodo == '❌':
                    fila_salto, col_salto = self.saltar_dos_veces(nueva_fila, nueva_col, direccion, self.pos_y)
                    self.tablero.cambiar_casilla(self.pos_y[0], self.pos_y[1], '🔳')
                    self.pos_y = (fila_salto, col_salto)
                    self.tablero.cambiar_casilla(fila_salto, col_salto, '🤖')
                    return

                else:
                    self.tablero.cambiar_casilla(self.pos_y[0], self.pos_y[1], '🔳')
                    self.tablero.cambiar_casilla(nueva_fila, nueva_col, '🤖')
                self.pos_y = (nueva_fila, nueva_col)
                return
            else:
                continue

    def bloqueo_x(self):
        while True:
            fila = int(input("Fila a bloquear ->  "))
            col = int(input("Columna a bloquear ->  "))

            if not self.tablero.verificar_posicion(fila, col):
                print()
                print("Posición invalida ")
                continue

            if self.tablero.obtener_posicion(fila, col) == '⛔':
                print()
                print("\nLa celda ya está bloqueada\n")
                continue

            if self.tablero.obtener_posicion(fila, col) == '🤖' or self.tablero.obtener_posicion(fila, col) == '❌':
                print("\nHay un jugador en la celda\n")
                continue

            self.tablero.cambiar_casilla(fila, col, '⛔')
            break

    def bloqueo_y(self):
        while True:
            fila = randint(0, self.tablero.tamano)
            col = randint(0, self.tablero.tamano)

            if not self.tablero.verificar_posicion(fila, col):
                continue

            if self.tablero.obtener_posicion(fila, col) == '⛔':
                continue

            if self.tablero.obtener_posicion(fila, col) == '🤖' or self.tablero.obtener_posicion(fila, col) == '❌':
                continue

            self.tablero.cambiar_casilla(fila, col, '⛔')
            break

    def verificar_ganador(self):
        if self.pos_x[0] == 0:
            return "\n!!!!!!!!!!!!!!!!El jugador X gana!!!!!!!!!!!!!!!"
        if self.pos_y[0] == self.tablero.tamano - 1:
            self.tablero.mostrar_tablero()
            return "\nLa maquina gana :( "
        else:
            return None
