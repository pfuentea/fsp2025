#esto es una lista , uno de los tipos iterables que posee Python
#usuarios_registrados=[]
#usuarios_registrados[0]='yerko'


#esto es un diccionario , otro de los tipos iterables que posee Python
usuarios_registrados={'yerko':28}
# un diccionario vacío se ve así:
# {}
# usuarios_registrados 
# {'yerko':28 ,'karina':18,'gloria':19 }
'''
paises = {
    'francia':
        {
        'capital':'paris',
        'habitantes':7000000,
        'superficie':50000,
    },
    'alemania': 
    {
        'capital':'berlin',
        'habitantes':10000000,
        'superficie':35000,
    }
}
'''

def registrar_usuario(nombre,edad):
    usuarios_registrados[nombre]=edad
    #usuarios_registrados.append(nombre)
    return True

def esta_registrado(nombre):
    if nombre in usuarios_registrados:
        return True
    else:
        return False
    
def es_mayor_de_edad(edad):
    if edad >= 18:
        return True
    else:
        return False