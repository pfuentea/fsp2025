'''
tabla de verdad de Y (and)
V y V = V
V y F = F
F y V = F
F y F = F

tabla de verdad de O (or)
V o V = V
V o F = V
F o V = V
F o F = F
'''
edad = int(input("Ingrese su edad:")) #25

if (edad < 50 and edad > 35):# verdadero Y falso = falso 
    print("adulto")

if (edad <25 ):
    print("menor a 25")
elif (edad >= 18):
    print("adulto")
elif (edad <30 and edad > 20):
    print("adulto joven")
else:
    print("menor")

#aca sigue ejecutando el programa