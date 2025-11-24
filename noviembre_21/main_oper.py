import operaciones

# from operaciones import sumar,restar

# Probar funciones
print("Suma:", operaciones.sumar(5, 3))
print("Resta:", operaciones.restar(10, 4))

# Usar la clase Calculadora
calc = operaciones.Calculadora() # se INSTANCIAR UN OBJETO DE TIPO Calculadora

print("Multiplicación:", calc.multiplicar(6, 7))
#esta operacion no se puede realizar a menos que se use con un OBJETO
#print(operaciones.multiplicar(6, 7))
print("División:", calc.dividir(20, 5))