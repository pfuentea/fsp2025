def obtener_servicio(opcion):
    respuestas={
        1:"Tu saldo es -$1.654.234",
        2:"Transferencias desde BancoEstafo a BancoChicle",
        3:"Pago de servicios:Agua, Luz, Gas, Internet",
        4:"Prestamos a tasa de 1,2% mensual",
        5:"Atención al cliente: llame al 600 600 600"
    }

    return respuestas.get(opcion,"Opción no valida, intente nuevamente")

def menu():
    servicios={
        1:"Consultar saldo",
        2:"Transferencias",
        3:"Pago de servicios",
        4:"Prestamos y créditos",
        5:"Atención al cliente",
        6:"Salir"
    }
    print("Seleccione una opción.")
    for llave in servicios:
        print(f"{llave}:{servicios[llave]}")

print("---==== Bienvenido al sistema de clientes ====---")
while(True):
    menu()
    opcion = int(input("Favor ingrese una opción (1-5):"))
    if opcion==6:
        break
    else:
        resp_servicio=obtener_servicio(opcion)
        print(f"--> {resp_servicio}")

print("---==== Gracias por utilizar el sistema ====---")