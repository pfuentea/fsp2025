if True:
    print("esto no se ejecutará")


try:
    print("Inicio del programa")
    dict={"nombre":"Jose"}
    print(dict["apellido"])
    print("esto no se verá")
except ValueError:
    print("El error es porque puso un valor mal")
except ZeroDivisionError:
    print("El error es porque puso cero en el divisor")
except KeyError:
    print("El error es porque tomo un indice que no existe")
except:
    print("Error inesperado")