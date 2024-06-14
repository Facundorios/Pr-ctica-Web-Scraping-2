# Description: Este script descarga imagenes de la pagina web de la NASA

# Importamos las librerias necesarias
import requests
from bs4 import BeautifulSoup as bs
import re
import os


# Definimos la funcion que descargara las imagenes
def guardar_imagenes(imagenes):
    # Nos aseguramos de que exisa la carpeta de imagenes, en caso de no ser así, se crea una.
    if not os.path.exists("imagenes"):
        os.makedirs("imagenes")
    # Iteramos sobre la lista de imagenes
    for i, img in enumerate(imagenes):
        # Hacemos una peticion a la url de la imagen
        response = requests.get(img)
        # Si la peticion fue exitosa, guardamos la imagen en la carpeta imagenes
        if response.status_code == 200:
            with open(f"imagenes/imagen_numero_{i}.jpg", "wb") as f:
                f.write(response.content)
        # Si la peticion no fue exitosa, mostramos un mensaje de error y salimos del bucle
        else:
            print(f"Error: {response.status_code}")
            break
    print(f"{len(imagenes)} imagenes guardadas!")


def obtener_imagenes(url):
    try:
        # Hacemos una peticion a la url
        response = requests.get(url)
        # Si la peticion no fue exitosa, lanzamos una excepcion
        if response.status_code != 200:
            raise Exception(f"Error: {response.status_code}")
        # Creamos un objeto BeautifulSoup
        soup = bs(response.text, "html.parser")
        results = soup.find_all("img")
        # Obtenemos las urls de las imagenes
        img_url = [img["src"] for img in results if "src" in img.attrs]
        # Filtramos las urls que no contengan .jpg, .png o .webp
        img_url = [
            img for img in img_url if re.search(r"\.jpg|\.png|\.webp", img) is not None
        ]
        # Eliminamos las urls duplicadas
        img_url = list(set(img_url))
        # Guardamos las imagenes
        guardar_imagenes(img_url)

    except Exception as e:
        print(f"Error: {e}")
        pass


imagenes_nasa = "https://www.nasa.gov/multimedia/imagegallery/iotd.html"
obtener_imagenes(imagenes_nasa)
