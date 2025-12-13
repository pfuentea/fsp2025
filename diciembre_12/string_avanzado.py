# Manipulación avanzada de strings
# strip () , lstrip(), rstrip()

texto="       Python avanzado     "
print(f"|{texto}|")
print(f"|{texto.strip()}|") # elimina los espacios a la derecha e izquierda
print(f"|{texto.lstrip()}|") # elimina los espacios a la izquierda
print(f"|{texto.rstrip()}|") # elimina los espacios a la derecha

# lower() , upper() , capitalize() , title() , swapcase()
nombre="franCiscO"
titulo="hola francisco gracias por venir"
print(f"{nombre.lower()}")  # convierte todo a minúscula
print(f"{nombre.upper()}") # convierte todo a mayúscula
print(f"{titulo.capitalize()}") # deja solo la letra inicial en mayúscula
print(f"{titulo.title()}") # cambia a mayúscula la primera letra de cada palabra
print(f"{titulo.swapcase()}") # intercambia mayúsculas por minúsculas y viceversa.

# replace(texto_que_busca,texto_que_reemplaza)
mensaje="Hola mundo"
nuevo_mensaje=mensaje.replace("o","0") #busca el primer argumento y lo reemplza por el segundo
print(nuevo_mensaje)

# startwith(), endswidth()  , entrega True o False
archivo="documento.pdf"
print(archivo.endswith(".pdf"))
print(archivo.startswith("doc"))

# join() 
palabras=["Hola","a","todos"]
frase=" ".join(palabras)
print(frase)

# split()  nos entrega una lista con los elementos separados
linea="nombre,apellido,edad,direccion,email"
cabecera=linea.split(",") # por defecto el caracter divisor es el espacio
print(cabecera)

texto="   Hola, me llamo Aureliano y me gusta Python!!    "
# 1.- Quitar espacios sobrantes al principio y al final
texto = texto.strip()
print(texto+"|")
# 2.- Convertir todo a minúsculas
print(f"{texto.lower()}")
# 3.- Reemplazar Aureliano por su nombre
ejercicio=texto.strip().lower().replace("aureliano", "yuri")
print(ejercicio)
# 4.- Verificar si el texto termina con "Python!!"
termina = texto.endswith("Python!!")
print (termina)
# 5.- Dividir el texto en palabras y mostar cuantas tiene
palabras = texto.split()
print(palabras)
print(len(palabras))
