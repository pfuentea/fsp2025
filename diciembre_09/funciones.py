#Parte 1 – Crear una función básica sin parámetros
# para definir una función se comienza con "def", luego el nombre y entre parentesis los parametros que necesita
def saludar():
    print("Hola, cómo estás?")

# para llamar o invocar una funcion simplemente usamos su nombre

saludar()
saludar()
saludar()
saludar()
saludar()
saludar()

#Parte 2 – Función que retorna un valor

def multiplicar(a,b): # entre parentesis van los PARAMETROS
    #print(a*b)
    return a*b

def mostar_lista(lista):
    for l in lista:
        print(f"->{l}")
    return True
'''
lista_alumno=['jose','pablo','lucia','amaranta']
lista_letras=['a','b','c','d']

numero1=int(input("Ingrese el primer número:"))
numero2=int(input("Ingrese el segundo número:"))

#cuando invocamos a la función 
resultado=multiplicar(numero1,numero2)
print(f"El resultado es:{multiplicar(numero1,numero2)}")
print(f"El resultado es:{resultado}")

resultado=mostar_lista(lista_alumno)
if resultado:
    print("El resultado fue correcto")
else:
    print("El resultado fue erroneo")

mostar_lista(lista_letras)

#Parte 3 – Crear una función con parámetros
def bienvenida(nombre):
    print(f"Hola {nombre}, bienvenido al mejor curso!")

condicion=True
iteracion=0

while condicion:
    usuario=input("Cual es tu nombre?:")
    if usuario =="":
        break
    bienvenida(usuario)
    iteracion+=1
    if iteracion >5:
        condicion=False
'''
def convertir_a_diccionario(tupla):
    new_dict={
        tupla[0]:tupla[1]
    }
    return new_dict

tupla_usuario=("USR001",6255321)

print(convertir_a_diccionario(tupla_usuario))

# al poner un parametro OBLIGATORIO, va al inicio de la
# definicion, luego los que son OPCIONALES
# Agregando un signo = con un valor por defecto, podemos
# dejar sin llenar ese valor al invocar a la función
def par_ordenado(repeticion,tupla = (0,0)  ):
    return tupla[0]*repeticion, tupla[1]*repeticion # si retorno más de un valor, se retorna como TUPLA

coordenada=(1,2)

x,y = par_ordenado(coordenada)
print(f"el valor de x es:{x}, el valor de y es:{y}")

# que pasa si no le paso nada como parametro? ->ERROR!!!!
z,w = par_ordenado(4)
print(f"el valor de x es:{z}, el valor de y es:{w}")

