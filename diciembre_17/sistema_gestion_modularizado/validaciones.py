def validar_nombre(nombre):
    nombre=nombre.strip()
    if len(nombre)<2:
        raise ValueError("El nombre debe tener más de 2 letras")
    return nombre

#validar correo
def validar_correo(email):
    if "@" not in email or "." not in email:
        raise ValueError("Email inválido!")

    return email

#validad edad
def validar_edad(edad):
    try:
        edad=int(edad)
    except ValueError:
        raise ValueError("Edad debe ser un número")
    
    if edad <0 or edad >120:
        raise ValueError("Edad fuera del rango 0-120")

    return edad
#validar rut
def validar_rut(rut):
    rut=rut.strip()
    if "-" in rut:
        numero,dv=rut.split("-")
        dv=dv.lower()
        if not numero.isdigit():
            raise ValueError("El rut no es correcto (1)")
        
        if dv == "" or ( not dv.isdigit() and dv !="k"):
            raise ValueError("El rut no es correcto (2)")
    else:
        raise ValueError("El rut debe tener guión")
    
    return f"{numero}-{dv}"
   