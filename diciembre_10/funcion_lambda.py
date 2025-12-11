

# lambda argumentos:expresion (la expresión tiene implicito un return)
suma = lambda a,b:a+b
resultado=suma(3,4)
print(f"El resultado es:{resultado}, {suma(34,45)}")

# pasar un número y que lo duplique x2
def multiplicar_x_2(x):
    return x*2

duplicar = lambda x : x*2

print(f"El resultado es:{duplicar(4)}")

# uso de lambda con map()
# list(map(funcion,iterable))
numeros=[1,2,3,4,5]
cuadrados = list(map(lambda x:x**2,numeros))
'''
1-->x=1 => 1
2-->x=2 => 4
3-->x=3 => 9
4-->x=4 => 16
5-->x=5 => 25
'''
print(cuadrados)

# uso de lambda con filter()
numeros=[1,2,3,4,5]
'''
1-->x=1 (1%2==0)=> False
2-->x=2 (2%2==0)=> True
3-->x=3 (3%2==0)=> False
4-->x=4 (4%2==0)=> True
5-->x=5 (5%2==0)=> False
'''
pares=list(filter(lambda x: x%2==0 ,numeros))
print(pares)

#otro ejemplo con lambdas y condicionales
lista_numeros=[-4,3,-5,2,1,-6]
# [-4,9,-5,4,1,-6]
resultado=list(map(lambda x:x**2 if x>0 else x ,lista_numeros))
print(resultado)

from functools import reduce
#Uso de reduce
valores=[1,2,3,4,5]
# 15
suma= reduce(lambda a,b: a+b ,valores)
print(suma)

# como hacemos la suma de 1 hasta n (n número entero)?
#by Sandra
n=10 #55
suma=reduce(lambda x,y:x+y, range(1,n+1))
print(suma)

numero=-10
suma=numero*(numero+1)/2
print(suma)



datos=[20,180,260,420]
# que me entrega esta expresión??
resultado=list(
    map(lambda x:x*2,
        filter(lambda x:x<300,datos)) # [20,180,260] 
)
# [20,180,260] ....Juan Manuel, Sandra
# [40] ...Constanza, Hernan
# [40, 360, 520] 
print(resultado)

#Range es un generador de números
