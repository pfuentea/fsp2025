# Crear un diccionario con los datos: nombre, edad, email
persona={
    "nombre":"Yerko",
    "edad":23,
    "email":"esperancito@gmial.com",
    "apellido":"arancibia",
}

#Acceder a valores usando claves (persona["nombre"])
print(f"Nombre:{persona["nombre"]}")
print(f"Edad:{persona["edad"]}" )
print(f"Email:{persona["email"]} " )

#Modificar un dato (por ejemplo, actualizar la edad)
persona["edad"]=28
print(f"Edad modificada:{persona["edad"]}" )

#imprimir una llave ingresada por consola
llave_objetivo=input("ingrese la llave a mostrar:")

if llave_objetivo in persona :
    print(f"El llave existe y su valor es:{persona[llave_objetivo]}" )
else:
    print("no existe la llave:",llave_objetivo)
#opcion 1 : no pasa nada
#opcion 2: manda un error
#opcion 3: se acaba el mundo

#Agregar un nuevo dato ("país": "Argentina")
persona["pais"]="Argentina"
print(persona)

#Eliminar un campo con pop() o del
persona.pop("email")
print("eliminamos email")
print(persona)

#Mostrar todas las claves, valores y pares con keys(), values(), items()

for claves in persona:
    print(claves)

for tupla in persona.items():
    print(tupla)

for keys,value in persona.items():
    print(f"LLAVE:{keys}, VALOR:{value}")

for valor in persona.values():
    print(f"VALOR:{valor}")

for llave in persona.keys():
    print(f"LLAVE:{llave}")
    print(f"VALOR:{persona[llave]}")

# Usar get() para obtener un dato sin error si no existe
name=persona.get('nombre')
print("el nombre es:",name)

#verificamos si lo obtenido con get() trajo un valor
correo=persona.get('email')
if correo is None:
    print("correo no existe")
else:
    print("el correo es:",correo)

nombre_yerko=persona['nombre']