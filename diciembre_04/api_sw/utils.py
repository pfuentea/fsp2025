# utils.py

def pedir_numero(mensaje):
    """
    Pide un número por consola y valida que sea un entero positivo.
    """
    while True:
        valor = input(mensaje)
        if valor.isdigit():
            return int(valor)
        print("⚠ Debes ingresar un número válido.\n")


def mostrar_menu_recursos(recursos):
    """
    Muestra un menú numérico a partir del diccionario de recursos
    que viene del endpoint raíz de la API.
    Ejemplo de recursos:
    {
        "films": "https://swapi.dev/api/films/",
        "people": "https://swapi.dev/api/people/",
        ...
    }
    """
    print("\n===== Star Wars API =====")
    print("Recursos disponibles:\n")

    # enumerate para numerar las opciones del menú
    for indice, (nombre, url) in enumerate(recursos.items(), start=1):
        print(f"{indice}. {nombre.capitalize():10} -> {url}")

    print("\n0. Salir")
    print("==============================")


def mostrar_diccionario(data):
    """
    Muestra un diccionario clave/valor en forma ordenada.
    Si alguna clave tiene listas o diccionarios anidados, se imprimen tal cual.
    """
    if not data:
        print("No hay datos para mostrar.")
        return

    print("\n=== Detalle del recurso ===")
    for clave, valor in data.items():
        print(f"{clave.capitalize():15}: {valor}")
    print("===========================\n")
