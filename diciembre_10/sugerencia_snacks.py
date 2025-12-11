calorias=[120,180,250,310,400]

categorias=list(map(lambda x: "Snack liviano" if x<150 else "Barrita energética" if x <=300 else "Smothie o batido" ,calorias))
# ["Snack liviano","Barrita energética","Barrita energética","Smothie o batido","Smothie o batido"]
print(categorias)

intensos=list(filter(lambda x : x>300,calorias))

# una función "normal" análoga sería:
def intenso(lista):
    resultado=[]
    for elemento in lista:
        if elemento > 300:
            resultado.append(elemento) 
    return resultado

# [310,400]
print(intensos)
