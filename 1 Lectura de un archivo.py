# Lectura de un archivo y conteo de líneas y palabras
try:
    with open("texto.txt", "r") as archivo:
        lineas = archivo.readlines()
        print(f"Número total de líneas: {len(lineas)}")
        for i, linea in enumerate(lineas, start=1):
            palabras = linea.split()
            print(f"Línea {i}: {len(palabras)} palabras")
except FileNotFoundError:
    print("El archivo 'texto.txt' no existe. Por favor, créalo primero.")