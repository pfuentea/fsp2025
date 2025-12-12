def sumar(a,b):
    return a+b
    #esta parte del código jamás será ejecutada
    if a>0:
        return b
    else:
        return a

print("Empieza la ejecución")
resultado= sumar(5,3)

def calcular(a,b):
    suma=a+b
    resta=a-b
    return suma,resta

res_suma, res_resta = calcular(10,5)
print(f"El resultado de la suma es:{res_suma}")
print(f"El resultado de la resta es:{res_resta}")

#variables locales vs variables globales


x=100 # variable global

def ejemplo():
    x=50 #variable local 
    print(f"Dentro de la función:{x}")

ejemplo()
print(f"Fuera de la función:{x}")
# solucion esperada: 50 , 100  Sandra y todo el curso

lista=list(range(1,6))
for elemento in lista:
    print(f"elemento:{elemento}")

print(f"elemento:{elemento}")

# calculo de factorial
#  8!  esto se lee como 8 factorial
#  8! = 8*7*6*5*4*3*2*1 = 8 *7! = 
#  7! = 7 * 6!
def factorial(n):
    if n==1:
        return 1
    return n* factorial(n-1)

    #return 8 * factorial(7) 
                # return 7 * factorial(6)
                            # return 6 * factorial(5)
                                        #return 5 * factorial(4)
#120
print(f"el factorial de 5 es:{factorial(5)}")

# calculo de fibonacci
# fib(5)= 1,1,2,3,5,8,13,21,34,55
# F(n)=F(n−1)+F(n−2)
def fibonacci(n):
    if n==2:
        return 1
    elif n==1:
        return 1
    return fibonacci(n-1)+fibonacci(n-2)

print(f"el termino N=5 de fibonacci es:{fibonacci(10)}")

# Parametros por defecto
def saludar_usuario(nombre="Invitado",edad=18):
    print(f"Hola {nombre} de {edad} años, bienvenido!!")

saludar_usuario()
saludar_usuario("Pepito")
saludar_usuario("Hernan",20)

# Parametros nombrados
def mostrar_usuarios(nombre,edad):
    print(f"Nombre:{nombre}, Edad:{edad}")

mostrar_usuarios(edad=30,nombre='José')

# parametros variables *args y **kwargs
def sumar(*numeros):
    print(sum(numeros))

sumar(1,2,3,4,5)
sumar(15,43)

def describir_usuario(**datos):
    for clave, valor in datos.items():
        print(clave,":",valor)

describir_usuario(nombre="pedro",ciudad="Valdivia",edad=13)

# Documentacion de funciones
def area_circulo(radio):
    """ Calcula el area de un circulo a partir del radio """
    return 3.14159* radio**2

help(area_circulo)

# que retorna un procedimiento???
def mostrar():
    print("hola")


resultado=mostrar()
print(resultado) # None

# funciones dentro de funciones
def crear_multiplicador(n):
    def multiplicar(x):
        return x*n
    return multiplicar

por_5 = crear_multiplicador(5) # setea el valor de n en 5

print(por_5(10))  # entrega 50 como resultado
