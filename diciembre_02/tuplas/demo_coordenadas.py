# 1.-Creación de tupla con coordenadas de una ciudad
ciudad_principal=("Santiago",-33.4489,-70.6693)

#2.- Mostrar coordenadas por pantalla
#3.- Acceder a latitud y longitud por el indice
print("Ciudad principal")
print(f"Nombre:{ciudad_principal[0]}")
print(f"Latitud:{ciudad_principal[1]}")
print(f"Longitud:{ciudad_principal[2]}")

#4.- intentar modificar la tupla
try:
    ciudad_principal[0]="Concepción"
except TypeError as e:
    print(f"Error:{e} , las tuplas son inmutables")

input("estamos en pausa, para continuar, presione enter")
#5.- reemplazar la tupla completa
ciudad_principal=("Valparaiso",-33.0472,-71.6127)
print("Cambiando la tupla")
print("Ciudad principal")
print(f"Nombre:{ciudad_principal[0]}")
print(f"Latitud:{ciudad_principal[1]}")
print(f"Longitud:{ciudad_principal[2]}")
#usar tuplas dentro de una lista, para multiples registros

ciudades_objetivo=[
    ("Lima",-12.0464,-77.0428),
    ("Buenos Aires",-34.6037,-58.3816),
    ("Cordoba",-31.4201,-64.1888),
]

#iterar sobre la lista de tuplas y mostrar las ciudades

for ciudad in ciudades_objetivo:
    print(f"La ciudad {ciudad[0]} esta en lat:{ciudad[1]}, long:{ciudad[2]}")

print("Esta es la segunda manera")   

for nombre,latitud,longitud in ciudades_objetivo:
    print(f"La ciudad {nombre} esta en lat:{latitud}, long:{longitud}")

