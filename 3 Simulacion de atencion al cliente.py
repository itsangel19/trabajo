from collections import deque

# Simulación de atención al cliente
cola = deque()

# Agregar clientes
cola.append("Cliente 1")
cola.append("Cliente 2")
cola.append("Cliente 3")
print("Cola inicial:", list(cola))

# Atender clientes
atendido = cola.popleft()
print("Atendido:", atendido)
print("Cola actual:", list(cola))