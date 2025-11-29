# BY GLORIA

pin_correcto = "1234"
intentos = 3

print("Bienvenido al cajero automático")

while intentos > 0:
    pin = input("Ingrese su PIN: ")

    if pin == pin_correcto:
        print("Acceso correcto. Bienvenido.")
        break            # termina el ciclo si esta correcto
    else:
        intentos -= 1
        print("PIN incorrecto. Intentos restantes:", intentos)

# Si se agotaron los intentos, informar bloqueo
if intentos == 0:
    print("Acceso bloqueado. Demasiados intentos fallidos.")