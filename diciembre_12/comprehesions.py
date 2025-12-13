cuadrados = [ x*x for x in range(1,11) ]
cuadrados_conjunto = { x*x for x in range(1,11) }  
print(cuadrados)
print(cuadrados_conjunto)

# filtrar elementos , por ejemplo pares
pares=[n for n in range(20) if n %2==0 ]
print(pares)

# limpiar y transformar datos
nombres=["  Ana  ","Pedro   ", "  lUis"]
datos_limpios=[item.strip().capitalize() for item in nombres ]
print(datos_limpios)

# filtrar valores de un diccionario
personas=[
    {"nombre":"Ana","edad":25},
    {"nombre":"Luis","edad":30},
    {"nombre":"Pedro","edad":15},
]

mayores=[ p["nombre"] for p in personas if p["edad"]>=18  ]
print(mayores)
# la forma analoga de realizar esta lista por comprensión es:
mayores=[]
for p in personas:
    if p["edad"]>=18 :
        mayores.append(p["nombre"])


print(mayores)

