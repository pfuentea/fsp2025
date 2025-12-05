# api_sw.py
import requests
import json
import os

BASE_URL = "https://swapi.dev/api/"

# endpoint

def guardar_json(nombre_archivo, data):
    """
    Guarda un diccionario en un archivo JSON dentro de la carpeta 'data'.
    """
    carpeta = "data"

    # Crear carpeta si no existe
    if not os.path.exists(carpeta):
        os.makedirs(carpeta)

    ruta = os.path.join(carpeta, nombre_archivo)

    with open(ruta, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

    print(f"Archivo guardado: {ruta}")


def get_root():
    """
    Obtiene el JSON raíz de la API, que contiene las rutas
    de los recursos disponibles (people, films, planets, etc.).
    También lo guarda en un archivo root.json.
    """
    try:
        response = requests.get(BASE_URL, timeout=5)
        response.raise_for_status()
        data = response.json()

        # Guardar el menú raíz en un archivo
        guardar_json("root.json", data)

        return data
    except requests.exceptions.HTTPError as e:
        print("Error HTTP:", e)
    except requests.exceptions.RequestException:
        print("Error al conectarse a la API")

    return None


def get_resource(resource, id=1):
    """
    Obtiene un recurso específico desde la API SWAPI.

    resource: nombre del recurso (string), por ejemplo:
              "people", "planets", "starships", "films", etc.
    id: número del recurso (int)
    """
    url = f"{BASE_URL}{resource}/{id}/"

    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()

        # Guardar JSON automáticamente por recurso
        nombre_archivo = f"{resource}_{id}.json"
        guardar_json(nombre_archivo, data)

        return data

    except requests.exceptions.HTTPError as e:
        print("Error HTTP:", e)
    except requests.exceptions.RequestException:
        print("Error al conectarse a la API")

    return None
