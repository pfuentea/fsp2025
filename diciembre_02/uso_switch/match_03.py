
def procesar(evento):
    match evento:
        case {"tipo":"compra","monto":m} if m >10000:
            print(f"Compra de alto valor:{m}")
        case {"tipo":"compra","monto":m} :
            print(f"Compra normal:{m}")
        case {"tipo":"error","codigo":c} | {"tipo":"fail","codigo":c}  :
            print(f"Error con codigo:{c}")
        case _:
            print("Evento desconocido")

log1={"tipo":"compra","monto":30000}
evento2={"tipo":"compra","monto":5000}
evento3={"tipo":"error","codigo":"404 not found"}
evento4={"tipo":"fail","codigo":"Not conected"}

procesar(log1)
procesar(evento2)
procesar(evento3)
procesar(evento4)




