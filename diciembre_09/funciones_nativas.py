datos=[10,20,30]

#Parte 1 – Funciones de conversión y tipo
print("len:",len(datos))
print(f"El último indice de la lista es el {len(datos)-1}")

#print(datos[3]) # nos salimos del rango de indices de la lista

#Parte 2 – Verificación de tipos
print(f"El tipo de dato de la lista es:{type(datos)}")
print(f"Isinstance es:{isinstance(datos,dict)}")

#Parte 3 – Colecciones
datos_tupla=tuple(datos)
print(datos)
print(datos_tupla)
frase="Esta es una frase que vamos a dividir por palabras"
palabras=frase.split()
print(palabras)

#Parte 4 – Entrada y salida
opcion=input("Ingrese la opcion:")
print(f"La opcion elegida es:{opcion}")

#Parte 5 – Números y rango
for valor in range(1,6):
    print(f"El valor es :{valor}")

#funcion anidada
print(f"Una lista condel 1 al 5 es:{list(range(1,6))}")

# redondear a 2 dígitos
resultado=15.4665
print(f"el resultado redondeado es:{round(resultado,2)}")
