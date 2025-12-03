
def validar_str(texto):
    if texto!="":
        return True
    return False
        
def validar_int(numero):
    try:
        valor=int(numero)
        return True
    except:
        return False

def validar_float(numero):
    try:
        valor=float(numero)
        return True
    except:
        return False
