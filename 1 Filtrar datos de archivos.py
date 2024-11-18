# Crear el archivo con datos iniciales
with open("datos.csv", "w") as archivo:
    archivo.write("Nombre,Edad,Estado\n")
    archivo.write("Pedro,30,Activo\n")
    archivo.write("María,25,Inactivo\n")
    archivo.write("Laura,27,Activo\n")
    archivo.write("Carlos,29,Activo\n")

# Leer y filtrar los datos activos
with open("datos.csv", "r") as archivo:
    lineas = archivo.readlines()

with open("activos.csv", "w") as archivo:
    archivo.write(lineas[0])  # Escribir el encabezado
    for linea in lineas[1:]:
        if "Activo" in linea:
            archivo.write(linea)

print("Archivo 'activos.csv' creado con los datos filtrados.")