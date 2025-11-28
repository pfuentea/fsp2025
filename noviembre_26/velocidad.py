velocidad_maxima=60

velocidad_actual=float(input("Ingrese su velocidad actual:"))

if velocidad_actual>velocidad_maxima:
    print("Atención:Excediste el límite de velocidad permitida")
    print("Por favor disminuye tu velocidad")
else:
    print("Gracias por ser una persona prudente")
