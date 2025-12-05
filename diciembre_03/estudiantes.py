#BY GLORIA

# Lista vacía
estudiantes = []

# Agregar al menos 5 estudiantes (nombre, edad, ciudad)
estudiantes.append(("Ana", 25, "Córdoba"))
estudiantes.append(("Luis", 30, "Mendoza"))
estudiantes.append(("María", 22, "Córdoba"))
estudiantes.append(("Jorge", 28, "Rosario"))
estudiantes.append(("Lucía", 35, "Salta"))

# Mostrar todos los registros
print("\n LISTADO DE ESTUDIANTES")
for nombre, edad, ciudad in estudiantes:
    print(f"Nombre: {nombre}, Edad: {edad}, Ciudad: {ciudad}")

# Consultar cuántos estudiantes son de una ciudad
ciudad_buscada = input("\nIngrese una ciudad para buscar: ")
contador = 0

for estudiante in estudiantes:
    if estudiante[2].lower() == ciudad_buscada.lower():
        contador += 1

print(f"\nHay {contador} estudiantes de {ciudad_buscada}")

# Calcular la edad promedio
total_edades = 0

for estudiante in estudiantes:
    total_edades += estudiante[1]

promedio = total_edades / len(estudiantes)

print(f"\nEdad promedio: {promedio:.2f} años")

# agregar nuevo estudiante
agregar = input("\n¿Desea agregar un nuevo estudiante? (si/no): ")

if agregar.lower() == "si":
    nombre = input("Nombre: ")
    edad = int(input("Edad: "))
    ciudad = input("Ciudad: ")
    estudiantes.append((nombre, edad, ciudad))
    print("\nEstudiante agregado con éxito 🎉")

print("\n PROGRAMA FINALIZADO\n")