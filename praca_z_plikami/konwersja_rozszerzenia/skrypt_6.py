"""
Napisz skrypt konwersji rozszerzeń plików *.jpg na *.png (up- rzednio stwórz zestaw 4 plików z rozszerzeniem *.jpg)
"""

import os
from PIL import Image

def convert_images():
    cwd_path = os.getcwd() # Assuming that running from .../PwJS-PiLB folder
    abs_path = os.path.join(cwd_path, 'praca_z_plikami/konwersja_rozszerzenia/images')
    images_names = os.listdir(abs_path)


    abs_images_names = [os.path.join(abs_path, image) for image in images_names if image != '.DS_Store']
    loaded_images_list = [Image.open(image) for image in abs_images_names]

    for i in range(len(loaded_images_list)):
        save_path = os.path.join(abs_path, 'converted_{i}.png'.format(i=i))
        loaded_images_list[i].save(save_path)

if __name__ == "__main__":
    convert_images()
    print('Conversion successful!')


