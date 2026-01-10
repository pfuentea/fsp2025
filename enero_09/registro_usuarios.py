#Jerarquía

class ErrorData(Exception):
    pass
class NombreVacioError(ErrorData):
    pass
class EdadNegativaError(ErrorData):
    pass
class EmailInvalidoError(ErrorData):
    pass

def valida_nombre(nombre):
    nombre=nombre.strip()
    if not nombre:
        raise NombreVacioError("El nombre no puede estar vacío")
    return nombre

def validad_edad(edad):
    try:
        edad=int(edad)
    except ValueError:
        raise ErrorData("La edad debe ser un entero")
    if edad <0:
        raise EdadNegativaError("La edad debe ser positiva")
    return edad

def valida_email(email):
    email=email.strip()
    if not email:
        raise EmailInvalidoError("Email no debe ser vacío")
    if "@" not in email:
        raise EmailInvalidoError("El email debe contener una @")
    return email

def registro():
    nombre=valida_nombre(input("Ingrese el nombre:"))
    edad=validad_edad(input("Ingrese la edad:"))
    email=valida_email(input("Ingrese el email:"))

    return {
        "nombre":nombre,
        "edad":edad,
        "email":email
    }


try:
    usuario=registro()
except NombreVacioError:
    print("Error en el nombre")
except EmailInvalidoError:
    print("Error en el email")
except EdadNegativaError:
    print("Error en la edad")
except ErrorData:
    print("Error en los datos")
finally:
    print("Fin del registro de usuario")