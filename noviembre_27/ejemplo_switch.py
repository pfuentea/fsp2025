def obtener_dia(numero):
    dias={
        1:"lunes",
        2:"martes",
        3:"miércoles",
        4:"jueves",
        5:"viernes",
        6:"sábado",
        7:"domingo"
    }
    return dias.get(numero,"Número inválido")

num=int(input("Ingrese un número (1-7): "))

if (num >=1 and num <=7):
    mensaje=f"El dia de la semana es:{obtener_dia(num)}"
else:
    mensaje=obtener_dia(num)

print(mensaje)