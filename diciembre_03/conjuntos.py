pedro='pedro'
lista_uno=['constanza','gloria','hector','hernan','juan manuel','hector','osvaldo']
lista_dos=['constanza','juan','karina','rafael','karina','juan','osvaldo']

print("Lista uno (con repetidos):",lista_uno)
print("Lista dos (con repetidos):",lista_dos)

conjunto_uno=set(lista_uno)
conjunto_dos=set(lista_dos)

print("Usuarios únicos conjunto uno:",conjunto_uno)
print("Usuarios únicos conjunto dos:",conjunto_dos)

#Intersección de conjuntos  
# a={1,2,3,4} b={3,4,5,6}  a & b={3,4}
interseccion=conjunto_uno & conjunto_dos
print("La intersección de conjunto uno y dos es:", interseccion)

if conjunto_uno & conjunto_dos:
    print("inter no es vacia")
else:
    print("inter vacia")

# Union de conjuntos  
# a={1,2,3,4} b={3,4,5,6}  a | b = {1,2,3,4,5,6}
union=conjunto_uno | conjunto_dos
print("La unión de conjunto uno y dos es:", union)

#diferencia de conjuntos
# a={1,2,3,4} b={3,4}  , a-b={1,2} , 
# b-a={3,4} hernan
# b-a={} sandra

a={1,2,3,4} 
b={3,4}
diferencia=conjunto_uno - conjunto_dos
diferencia_2= b - a
print("La diferencia de conjunto uno y dos es:", diferencia)
print("La diferencia de conjunto dos y uno es:", diferencia_2)

#usar add y remove
print("----modificando los conjuntos----")
print("Conjunto uno antes de agregar a sandra:",conjunto_uno)
conjunto_uno.add('sandra')
print("Conjunto uno luego de agregar a sandra:",conjunto_uno)
# se puede usar remove(), pero si no existe el elemento se cae el programa
conjunto_uno.discard('gloria')

#conjunto_uno.remove('yuri')
elemento=conjunto_uno.discard('yuri')

print("Conjunto uno luego de quitar a gloria:",conjunto_uno)

a={1,2,3,4} 
b={3,4,5,6}

c=a.union(b) # a|b  "or de patrones" == union == OR == + 
print("conjunto c:",c) 

#recorrer un conjunto con un for
for elemento in conjunto_uno:
    print("->",elemento)

