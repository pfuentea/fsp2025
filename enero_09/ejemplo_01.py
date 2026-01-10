class ErrorAplication(Exception):
    pass
class ErrorValidation(ErrorAplication):
    pass
class ErrorPermisos(ErrorAplication):
    pass

def verificar_usuario(rol):
    if rol == "visitante":
        raise ErrorPermisos("Acceso no autorizado")
    elif rol not in ["admin","editor"]:
        raise ErrorValidation("Rol invalido")
    
try:
    verificar_usuario("visitante")
except ErrorPermisos:
    print("No tienes permisos suficientes")
except ErrorValidation:
    print("Datos inválidos")
except ErrorAplication:
    print("Otro error general de aplicación")
