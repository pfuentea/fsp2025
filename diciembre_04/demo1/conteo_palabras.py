#Solicitar al usuario que ingrese una frase
frase=input("Ingrese una frase por favor:")
#Dividir la frase en palabras usando .split()
palabras = frase.split()
#Crear un diccionario vacío llamado frecuencia
frecuencia={}
#Recorrer las palabras con un for
#Usar get() para contar cuántas veces aparece cada palabra
#Guardar cada conteo como clave: valor (palabra: cantidad)

for palabra in palabras:
    frecuencia[palabra.lower()]=frecuencia.get(palabra.lower(),0) + 1

#Imprimir el diccionario final con las frecuencias
print(frecuencia)

#Bonus: Ordenar el diccionario por frecuencia descendente
# sorted (lo_que_quiero_ordenar, por_que_campo_quiero_ordenar,reverse=False => ascendente y reverse=True => descendente)

# frecuencia.items() => ("Hoy",1), Hoy esta en la posicion 0 y 1 esta en la posicion 1
lista_ordenada=sorted(frecuencia.items(),key=lambda x:x[1], reverse=True)
print("aca debe haber una lista ordenada por frecuencia descendente")
print(lista_ordenada)
# aqui transformamos la lista a diccionario
diccionario_ordenado = dict(lista_ordenada)
print("aca debe haber un diccionario ordenado por frecuencia descendente")
print(diccionario_ordenado)

#By Sandra
#Hoy elegi el camino del odio , odio a todos , en especial a quienes les gusta Star Wars