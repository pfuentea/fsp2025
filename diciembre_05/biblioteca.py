# BY HERNAN
libros={
    "B001":{"titulo":"El Método pellegrini","autor":"Francisco Sagredo, 1975","genero":"biografía deportiva","stock":30},
    "B002":{"titulo":"Los Chicos de la guerra","autor":"Daniel Kon, 1956","genero":"drama","stock":30},
	"B003":{"titulo":"El tercer ojo","autor":" Lobsang Rampa, 1910","genero":"exoterismo","stock":20},
    "B004":{"titulo":"Barrio Bravo","autor":" Roberto Meléndez, 1985","genero":"crónicas de futbol","stock":30},
    "B005":{"titulo":"El código da Vinci","autor":"Dan Brown, 1964","genero":"Thriller de Misterio","stock":30},
}

def get_codigo():
    id_prod=input("El código del libro:").upper()
    print(f"-{id_prod}-")
    if id_prod in libros:
        return id_prod
    else:
        print("codigo del libro no existe!")
        return False

def menu():
    print("--------Menú Principal de la biblioteca--------")
    print("-----------------------------------------------")
    print("1: Agregar un nuevo libro")
    print("2: Actualizar stock de un libro")
    print("3: Eliminar un libro del stock")
    print("4: Mostrar todos los libros disponibles")
    print("5: Mostar libros con stock menor a 3 unidades")
    print("6: Permite hacer búsqueda por género")
    print("--------Seleccione una opción--------")
    print("99: para salir")

while True:
    menu()
    opcion=input("Ingrese una opción:")
    
    if opcion=="99":
        print("Gracias por usar nuestro sistema, hasta la próxima vez!")
        break
    #Agregar un nuevo libro al diccionario
    elif opcion=="1":
        print("Ingrese los datos del nuevo libro")
        v_titulo=input("Título :")
        v_autor=input("Autor :")
        v_year=input("Año nacimiento del autor : ")
        v_genero=input("Género :")
        v_stock=int(input("Stock (numeros enteros): "))
                                            
        v_ult_clave = max(libros.keys(), key=lambda k: int(k[1:]))
        parte_num = v_ult_clave[1:]
        num = int(parte_num) + 1
        v_new_clave = "b" + f"{num:0{len(parte_num)}d}"
                                           
        try:
            libros[v_new_clave.upper()]={
                "titulo":v_titulo,
                "autor": v_autor+","+ v_year,
                "genero":v_genero,
                "stock":int(v_stock),
                }
        except ValueError as e:
            print("Debe ingresar un número:",e)
        except IndexError as e:
            print("Debe ingresar 3 elementos:",e)

    elif opcion=="2": #modificar stock
        # pedir el id del libro -> id_prod
        id_prod=get_codigo()
        if id_prod:
        #pedir el nuevo stock
            try:
                nuevo_stock=int(input("Ingrese el nuevo stock:"))
                libros[id_prod]["stock"] =nuevo_stock
            except:
                print("stock incorrecto")

                    
    elif opcion=="3":
        #eliminar libro
        # pedir el id libro -> id_prod
        id_prod=get_codigo()
        if id_prod:
            libros.pop(id_prod)

    elif opcion=="4":
        #ver todos los libros
        for id_prod,libro in libros.items():
            print(f"Código :{id_prod}")
            print(f"Título :{libro["titulo"]}")
            print(f"Autor :{libro["autor"]}")
            print(f"Género :{libro["genero"]}")
            print(f"Stock :{libro["stock"]}")
            print("--------------------")