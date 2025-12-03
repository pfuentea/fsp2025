# MATCH (Structural Pattern Maching)

''' sintaxis de MATCH
variable_a_evaluar =10
match variable_a_evaluar:
    case valor1:
        instrucciones_1
    case valor2:
        instrucciones_2
    case valor3:
        instrucciones_3
    case valor_n:
        instrucciones_n
    case _:
        instruciones_pod_default
'''
absisas=int(input("Ingrese el punto en X:"))
ordenadas=int(input("Ingrese el punto en Y:"))
punto=(absisas,ordenadas)

match punto:
    case (0,0):
        print("Origen")
    case (x,0):
        print(f"Sobre el eje x,x={x}")
    case (0,y):
        print(f"Sobre el eje y,y={y}")
    case _:
        print("cualquier otro punto")