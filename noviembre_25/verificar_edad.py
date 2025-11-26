# BY YURI

edad = int(input("estimado ingrese la edad: "))

if edad < 0 :
    print("numero invalido, La edad debe ser mayor o igual a cero.")    
elif edad <= 12 :
    print("escolar(niñ@).")  
elif edad <= 17:
    print("adolescente.")
elif edad <= 64:
    print("adulto.")
else:
    print("adulto mayor.")