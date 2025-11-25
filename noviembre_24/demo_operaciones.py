# al inicializar las variables quedan de tipo INT
a=15
b=8
c=5
d=-45

a2="15"

resultado1 = a + b #23
resultado2 = b * c #40
resultado3 = a / b # 1.875 , división flotante
resultado4 = a % b # 7
resultado5 = a // b # 1 , división entera

print(f"resultado1:{resultado1}") 
print(f"resultado2:{resultado2}")
print(f"resultado3:{resultado3}")
print(f"resultado4:{resultado4}")
print(f"resultado5:{resultado5}")

print(dir(resultado1))

print(abs(d)) #45