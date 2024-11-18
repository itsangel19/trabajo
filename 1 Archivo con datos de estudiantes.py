# Creación de archivo con datos de estudiantes
with open("estudiantes.txt", "w") as archivo:
    archivo.write("Nombre,Edad,Grado\n")
    archivo.write("Ana,13,Segundo\n")
    archivo.write("Juan,14,Tercero\n")
    archivo.write("Luis,16,Cuarto\n")
    archivo.write("Pedro,17,Quinto\n")

# Lectura del archivo e impresión de los datos
with open("estudiantes.txt", "r") as archivo:
    encabezado = archivo.readline()
    print("Información de estudiantes:")
    for linea in archivo:
        nombre, edad, grado = linea.strip().split(",")
        print(f"Estudiante: {nombre}, Edad: {edad}, Grado: {grado}")