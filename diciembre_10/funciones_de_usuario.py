def multiplicar (a,b) :
    return a*b

resultado= multiplicar(3,4)
print(f"El resultado de la multiplicación es:{resultado}")

def saludar():
    print("hola!")

def saludo():
    return "Hola!"

def ambos_saludos():
    print("hola!")
    return "Hola!"

def saludo_2(nombre,apellido):# nombre y apellido son PARAMETROS
    saludo=f"Hola {nombre} {apellido}"
    print(saludo)

#puedo invocarla y me imprime el saludo
#saludar()
#necesito usar print, ya que la función me retorna un string
#print( saludo() )

#ambos_saludos()
#print(ambos_saludos())
username='Pedro'
lastname='Gonzalez'
saludo_2(username,lastname) # 'Pedro' y 'Gonzalez' son ARGUMENTOS


#BY Yuri
def celsius_a_fahrenheit(Celcius):
    Fahrenheit = Celcius * (9/5) + 32
    return Fahrenheit


def area_triangulo(base, altura):
    area = (base * altura) / 2
    return area

#by Costanza
def celsius_a_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

#By Gloria
def celsius_a_fahrenheit(celsius):
    fahrenheit = celsius * 9/5 + 32
    return fahrenheit

temp_celcius = 100
temp_Fahrenheit = celsius_a_fahrenheit(temp_celcius)
print(f"{temp_celcius}°C son equivalentes a {temp_Fahrenheit}°F")


base=5
altura=4

print(f"El triangulo de base:{base} y altura:{altura} tiene como area:{area_triangulo(base,altura)}")

#by Sandra
#n=float(input('Ingrese la temperatura en grados c:'))
n=25
def c_a_f(celsius):
    return celsius * 9/5 + 32

print(f"{n}°C en Fahrenheit es: {c_a_f(n)}")

print(f"{n}°C en Fahrenheit es: {c_a_f(n)}")

print("25°C en Fahrenheit es:", c_a_f(n)," otro texto")

print(n+"°C en Fahrenheit es:"+c_a_f(n)+" .")

print("%d °C en Fahrenheit es:%d" %(n , c_a_f(n) ))