# Verificar balanceo de paréntesis usando una pila
def verificar_balanceo(cadena):
    pila = []
    for caracter in cadena:
        if caracter == "(":
            pila.append(caracter)  # Push
        elif caracter == ")":
            if not pila:
                return False
            pila.pop()  # Pop
    return len(pila) == 0

expresion1 = "(a + b) * (c + d)"
expresion2 = "(a + b * (c - d)"
print(f"Expresión 1: {'Balanceada' if verificar_balanceo(expresion1) else 'No balanceada'}")
print(f"Expresión 2: {'Balanceada' if verificar_balanceo(expresion2) else 'No balanceada'}")