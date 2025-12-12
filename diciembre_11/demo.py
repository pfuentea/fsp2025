# 1. Definición de un procedimiento:
def mostrar_mensaje():
    print("Este es un procedimiento, no devuelve nada.")

#2. Llamar al procedimiento:
mostrar_mensaje() # para llamar o invocar el procedimiento

#3. Procedimiento con parámetros:
def imprimir_lista(lista):
    print("Lista de elementos:")
    for item in lista:
        print(f"->{item}")

lenguajes=['Python','Html','Java','C++','Visual']
comunas=['La Ligua','Pudahuel','Villa Alemana','Penco']
imprimir_lista(lenguajes)
imprimir_lista(comunas)

# 4.Crear un procedimiento que imprima los detalles de un usuario:
def imprime_detalles(users):
    for usuario in users:
        print(f"Nombre:{usuario["nombre"]}")
        print(f"Apellido:{usuario["apellido"]}")
        print(f"Edad:{usuario["edad"]}")

usuarios=[
    {"nombre":"Pedro", "apellido":"Gonzalez","edad":28},
    {"nombre":"Juan", "apellido":"Lopez","edad":11},
    {"nombre":"Laura", "apellido":"Saavedra","edad":27},
    {"nombre":"Diego", "apellido":"Muñoz","edad":25},
    {"nombre":"Sandra", "apellido":"Alvarez","edad":15},
]

imprime_detalles(usuarios)

#Crear un procedimiento que verifique la edad: usando la misma lista de arriba
# By Gloria
def verifica_edad(usuarios):
    for usuario in usuarios:
        if usuario["edad"] >= 18:
            print(f"{usuario['nombre']} es mayor de edad.")
        else:
            print(f"{usuario['nombre']} es menor de edad.")

verifica_edad(usuarios)