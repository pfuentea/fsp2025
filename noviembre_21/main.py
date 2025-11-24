# de esta manera también podemos importar el código desde registro.py
# import registro

from registro import esta_registrado, registrar_usuario, es_mayor_de_edad

nombre = input("Ingresa tu nombre:")
edad = input("Ingresa tu edad:")

if esta_registrado(nombre) :
    print(f"El usuario {nombre} está registrado.")
    print("otra")
else :
    registrar_usuario(nombre, edad)
    print(f"El usuario {nombre} se registró exitosamente.")

if edad < 15:
    print("eres un niño")
    print("eres un niño")
    print("eres un niño")
    print("eres un niño")
    print("eres un niño")
    print("eres un niño")
    print("eres un niño")
elif edad >=15 and edad < 18:
    print("eres adolescente")
elif edad >=18 and edad < 30:
    print("eres adulto joven")
else:
    print("eres adulto")

print(f"Bienvenido a nuestra app {nombre}")


