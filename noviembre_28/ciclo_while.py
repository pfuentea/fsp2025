# adivinador de numero

menor=0
mayor=20
numero=(menor+mayor)//2

print(f"piense un número del 1 al {mayor}")

while True:
    respuesta=input(f"Su número es el {numero}?(s/n)")
    if respuesta=="s":
        print("Soy el mejor adivinando!")
        break
    else:
        respuesta2=input("Su número es mayor(u) o es menor(m)?")
        if respuesta2=="u":
            menor=numero
        elif respuesta2=="m":
            mayor=numero
        
        numero=(menor+mayor)//2
