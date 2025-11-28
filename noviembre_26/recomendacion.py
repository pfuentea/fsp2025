
temperatura= float(input("Ingrese la temperatura del día:"))


print(f"Para la temperatura {temperatura}, le recomendamos:")
if temperatura <10:
    print("Abrigo grueso y bufanda")
elif temperatura <= 20:
    print("Chaqueta ligera")
elif temperatura <= 30:
    print("Ropa comoda y fresca")
else:
    print("Ropa ligera y protector solar")
 