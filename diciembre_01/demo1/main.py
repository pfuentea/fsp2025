#from modulos.operaciones import sumar
from  modulos import *

opcion=input("Elija que quiere sumar: (s)String o (e)Enteros o (v)Vectores:")

if opcion == "s":
    str1 = input("Ingrese el primer STRING:")
    str2 = input("Ingrese el segundo STRING:")
    print(f"La suma de los Strings es: {sumar(str1,str2,"s")}")
elif opcion =="e":
    num1 = int(input("Ingrese el primer número ENTERO:"))
    num2 = int(input("Ingrese el segundo número ENTERO:"))
    print(f"La suma de los números es: {sumar(num1,num2,"e")}")
elif opcion =="v":
    vec1 = int(input("Ingrese el primer Vector:"))
    vec2 = int(input("Ingrese el segundo Vector:"))
    print(f"La suma de los números es: {sumar(vec1,vec2,"v")}")


