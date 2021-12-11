import requests
from PIL import Image
import os


def upscale(img, ratio = 9):
    """ Upscale the image by the ratio factor """
    width, height = img.size
    return img.resize((width * ratio, height * ratio))

def main():
    absolute_path = os.path.dirname(__file__)

    with open(f"{absolute_path}/namelist.txt") as file:
        pokemon_list = file.read().splitlines()
    
    for i, pokemon in enumerate(pokemon_list):
        url = "https://img.pokemondb.net/sprites/sword-shield/icon/" + pokemon + ".png"

        img = Image.open(requests.get(url, stream=True).raw)

        # Remove surrounding whitespaces from image
        img = img.crop(img.getbbox())

        img = upscale(img)

        img.save(f"./images/{pokemon}.png")
        
        print(f"[{i + 1}/898] {pokemon} saved!")

if __name__ == "__main__":
    main()