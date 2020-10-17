import os
from PIL import Image

def convert_images(path):
    abs_path = os.path.abspath(path)
    images_names = os.listdir(abs_path)

    abs_images_names = [os.path.join(abs_path, image) for image in images_names if image != '.DS_Store']
    loaded_images_list = [Image.open(image) for image in abs_images_names]

    for i in range(len(loaded_images_list)):
        save_path = os.path.join(abs_path, 'converted_{i}.png'.format(i=i))
        loaded_images_list[i].save(save_path)

if __name__ == "__main__":
    print('Current working directory: {cwd}'.format(cwd=os.getcwd()))
    path = input('Provide path to images folder: ')

    convert_images(path)
    print('Conversion successful!')


