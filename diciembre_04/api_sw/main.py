# main.py
from api_sw import get_root, get_resource
from utils import pedir_numero, mostrar_menu_recursos, mostrar_diccionario


def main():
    # Primero obtenemos el menú raíz desde la API
    recursos = get_root()

    if not recursos:
        print("No se pudieron obtener los recursos de la API.")
        return

    # Convertimos las claves en una lista para poder indexarlas por número de opción
    nombres_recursos = list(recursos.keys())

    while True:
        # Mostrar menú basado en el JSON raíz
        mostrar_menu_recursos(recursos)

        opcion = pedir_numero("Selecciona una opción: ")

        if opcion == 0:
            print("¡Hasta la próxima, joven Padawan!")
            break

        # Validar que la opción esté en rango
        if 1 <= opcion <= len(nombres_recursos):
            recurso_seleccionado = nombres_recursos[opcion - 1]
            print(f"\nHas elegido el recurso: {recurso_seleccionado}")

            # Pedimos ID del recurso
            id_recurso = pedir_numero(
                f"Ingrese el ID que quieres consultar para '{recurso_seleccionado}': "
            )

            # Obtenemos el recurso específico
            data = get_resource(recurso_seleccionado, id_recurso)

            # Mostramos los datos como diccionario
            mostrar_diccionario(data)

        else:
            print(" Opción inválida, intenta nuevamente.\n")


if __name__ == "__main__":
    main()
