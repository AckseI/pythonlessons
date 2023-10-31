"""
Написать функцию, которая принимает путь к изображению и выполняет
над ней autocontrast, сохраняя новое изображение по тому же пути.
"""

from PIL import Image
from PIL import ImageOps

def autocontrast(path_to_img):
    img_obj = Image.open(path_to_img)
    new_img_obj = ImageOps.autocontrast(img_obj, cutoff=5)
    new_img_obj.save('img/acon_img.png')

path_to_img = 'img/1.png'

autocontrast(path_to_img)
