valor_entrada=5000
tipo_usuario=input("Ingrese el tipo de usuario:")

descuento=0

if tipo_usuario=="jubilado":
    descuento=0.3
elif tipo_usuario=="estudiante":
    descuento=0.2
elif tipo_usuario=="regular":
    descuento=0
else:
    print("Tipo de usuario no válido")

# 1-0.3 = 0.7
# 1-0.2 = 0.8

precio_final=valor_entrada*(1-descuento)

print(f"Precio base:{valor_entrada}")
print(f"Descuento:{descuento*100}%")
print(f"Precio final:{precio_final}")

