
m = [["x",2,3],[4,5,6],[7,8,"y"]]

m2 = [["x",2,3,9,78],
      [4,"#","#","#", 5],
      [7,8,123,45,2],
      [4,7,32,1,5],
      [9,8,45,2,"y"]]

def recorrer(m, i_pos, f_pos, current,  caminos, l=[]):
    fila, col = current

    if fila < 0 or fila >= len(m) or col < 0 or col >= len(m[0]):
        return
    l.append(current)

    if current == f_pos:
        caminos.append(list(l))
        print(caminos)
        l.pop() 
        return

    recorrer(m, i_pos, f_pos, (fila + 1, col), caminos, l)

    recorrer(m, i_pos, f_pos, (fila, col + 1), caminos, l)

    l.pop()

def camino_mas_corto(m, i_pos, f_pos, current,  caminos, l=[]):
    fila, col = current

    # Verificar si la posición actual es válida
    if fila < 0 or fila >= len(m) or col < 0 or col >= len(m[0]) or m[fila][col] == "#":
        return

    # Agregar la posición actual al camino
    l.append(current)

    if current == f_pos:
        # Hemos llegado a la posición de destino
        caminos.append(list(l))  # Agregar una copia del camino actual a la lista de caminos
        l.pop()  # Eliminar la posición actual del camino
        return

    # Moverse hacia abajo
    recorrer(m, i_pos, f_pos, (fila + 1, col), caminos, l)

    # Moverse hacia la derecha
    recorrer(m, i_pos, f_pos, (fila, col + 1), caminos, l)

    # Eliminar la posición actual del camino antes de retroceder
    l.pop()

# recorrer(m, (0,0), (2,2), (0,0), [])


class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def agregar_elemento(self, valor):
        nuevo_nodo = Nodo(valor)
        nuevo_nodo.siguiente = self.cabeza
        self.cabeza = nuevo_nodo

def existe_camino(lista_principal, inicio, final, visitados=set()):
    if inicio == final:
        return True

    if inicio in visitados:
        return False

    visitados.add(inicio)
    nodo_actual = lista_principal.cabeza

    while nodo_actual:
        lista_enlazada_interna = nodo_actual.valor
        nodo_interno = lista_enlazada_interna.cabeza

        while nodo_interno:
            siguiente_posicion = nodo_interno.valor
            if existe_camino(lista_principal, siguiente_posicion, final, visitados):
                return True

            nodo_interno = nodo_interno.siguiente

        nodo_actual = nodo_actual.siguiente

    return False

# Ejemplo de uso
lista1 = ListaEnlazada()
lista1.agregar_elemento(1)
lista1.agregar_elemento(2)
lista1.agregar_elemento(3)

lista2 = ListaEnlazada()
lista2.agregar_elemento(4)
lista2.agregar_elemento(5)

lista3 = ListaEnlazada()
lista3.agregar_elemento(6)

lista_principal = ListaEnlazada()
lista_principal.agregar_elemento(lista1)
lista_principal.agregar_elemento(lista2)
lista_principal.agregar_elemento(lista3)

inicio = 1
final = 7

if existe_camino(lista_principal, inicio, final):
    print("Existe un camino entre", inicio, "y", final)
else:
    print("No existe un camino entre", inicio, "y", final)
