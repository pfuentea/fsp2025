diccionario1={
    "tipo":"login",
    "usuario":"sandra"
}
diccionario2={
    "tipo":"error",
    "mensaje":"contraseña incorrecta"
}

def validar(evento):
    match evento:
        case {"tipo":"login","usuario":u}:
            print(f"El usuario {u} inició sesión")
        case {"tipo":"error","mensaje":m}:
            print(f"Error:{m}")
        case _:
            print("Evento desconocido")

validar(diccionario1)
validar(diccionario2)