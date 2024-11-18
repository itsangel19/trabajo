# Revertir una cadena usando una pila
def revertir_cadena(cadena):
    pila = []
    for caracter in cadena:
        pila.append(caracter)  # Push
    cadena_revertida = ""
    while pila:
        cadena_revertida += pila.pop()  # Pop
    return cadena_revertida

cadena = "Python"
print(f"Cadena original: {cadena}")
print(f"Cadena revertida: {revertir_cadena(cadena)}")