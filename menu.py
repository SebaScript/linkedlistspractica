from random import randint
from tablero import Tablero
from juego import Juego


def menu_crear_tablero():
    while True:
        tamano_tablero = int(input("\nIngresa el tamaño del tablero: "))
        print("")
        if tamano_tablero < 3:
            print("El tablero debe ser minimo de 3x3")
            continue
        tablero = Tablero(tamano_tablero)
        juego = Juego(tablero)
        menu_inicio(tablero, juego)

def menu_inicio(tablero, juego):
    while True:
        opcion = input("Menú del juego\n1. Iniciar\n2. Salir\n-> ")
        print("\n Iniciando el juego \n")
        if opcion == "1":
            tablero.celdas()
            juego.iniciar_x()
            juego.iniciar_y()
            menu_turnos(tablero, juego)
            break

        elif opcion == "2":
            break

        else:
            print('Opción invalida, ingrese 1 o 2')
            continue

def menu_turnos(tablero, juego):
    while True:
        tablero.mostrar_tablero()

        print("\nTurno del jugador X\n")
        opcion_x = input("1. Moverse\n2. Bloquear casilla\n-> ")
        if opcion_x == "1":
            juego.movimiento_x()
        elif opcion_x == "2":
            juego.bloqueo_x()
        
        ganador = juego.verificar_ganador()
        if ganador:
            print(ganador)
            quit()
        
        print("\nTurno de la maquina\n")

        opcion_y  = str(randint(1, 2))
        if opcion_y  == "1":
            juego.movimiento_y()
        if opcion_y  == "2":
            juego.bloqueo_y()
        
        ganador = juego.verificar_ganador()
        if ganador:
            print(ganador)
            quit()

        menu_turnos(tablero, juego)


menu_crear_tablero()
