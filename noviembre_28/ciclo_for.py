ciudades_objetivo=['paris','madrid','berlin','rancagua','talca','concepcion','valparaiso','valdivia']

#for ciudad in ciudades_objetivo:
#    print(f"La cuidad objetico será:{ciudad}")

# enumerate nos entrega una TUPLA (indice,valor) 

#for indice,ciudad in enumerate(ciudades_objetivo, start=1 ):
#    print(f"{indice}.-La cuidad objetico será:{ciudad}")

print(ciudades_objetivo[3]+"-"+ciudades_objetivo[5])

for indice,ciudad in enumerate(ciudades_objetivo ):
    print(f"{indice+1}.-La cuidad objetico será:{ciudades_objetivo[indice]}")

# uso del range con 1 parámetro
for indice in range(5):
    print(f"el valor del indice es {indice}")

# uso del range con 2 parámetro
for indice in range(1,5):
    print(f"el valor del indice es {indice}")

print("================================")
# uso del range con 3 parámetro
indice_inicial=1
limite=10
paso=2
# para generar secuencia regresiva desde 10 hasta el 1 de 2 en 2
#indice_inicial=10
#limite=1
#paso=-2
for indice in range(indice_inicial,limite,paso):
    print(f"El valor del indice es {indice}") 

# generar una lista de numeros
numeros_del_1_al_100=list(range(1,101))

print(numeros_del_1_al_100)

letras=[chr(i) for i in range(65,91)]
letras2=[chr(i) for i in range(97,123)]
todas_las_letras=letras+letras2

print(todas_las_letras)

diccionario={
    "nombre":"constanza",
    "edad":21,
    "ciudad":"puerto octay",
    "rut":"20.656.872-1"
}
# para iterar un diccionario obteniendo sus llaves y valores
for llave,valor in diccionario.items():
    print(llave,"=>",valor)
# para iterar un diccionario obteniendo sus llaves
for llave in diccionario.keys():
    print(llave)
    print(f"valor:{diccionario[llave]}")
# para iterar un diccionario obteniendo sus valores
for valor in diccionario.values():
    print(valor)