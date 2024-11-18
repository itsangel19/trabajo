# Ordenar una cola usando listas
from collections import deque
def ordenar_cola(cola):
    return deque(sorted(cola))

cola = deque([5, 2, 8, 3, 1])
print("Cola original:", list(cola))
cola_ordenada = ordenar_cola(cola)
print("Cola ordenada:", list(cola_ordenada))