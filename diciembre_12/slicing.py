# Obtener los primeros caracteres
# [inicio:fin:paso] , [inicio,fin] []
texto="Python" 
print(texto[0:3]) #recordar que los string parten en el indice 0

# Pyt : Hernan
# Pyth : Sandra, Constanza

print(texto[-3:]) # si no hay nada es hasta el final
print(texto[-3]) # me trae h, ya que es un indice específico

#  0  1  2  3  4  5 
#  P  y  t  h  o  n
# -6 -5 -4 -3 -2 -1
# hon : Jocelyne , Karina, Sandra
# nohtyP : Yuri
# pyt : Hernan 
# h : Constanza 

print(texto[::-1]) # desde el inicio al fin, pero al revés
print(texto[-1 : :-2]) # de 2 en 2 en el indice

# listas parten en el indice 0
numeros=[10,20,30,40,50]
print(numeros[1:4]) 
# [10,20,30,40] : Hernan
#[20, 30, 40] : Juan Manuel,Sandra
print(numeros[ : :2]) 
# [10,30,50] 
print(numeros[ : :-1]) # lista invertida

palabra="desarrollador"
lista_numeros=[1,2,3,4,5,6,7,8]

# ejercicios para trabajar en casa (Tarea para la casa)
# los primeros 5 caracteres de la palabra
# los últimos 4 caracteres de palabra
# la palabra invertida
# Los números en posición PAR
# los números del 3 al 6 (inclusive)

