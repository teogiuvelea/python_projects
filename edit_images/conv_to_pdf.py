from PIL import Image 
import os

path = "cropped_img/"
dir_list = os.listdir(path)
print(dir_list)

img_names = dir_list


ls_imgs = []
for name in img_names:
    print(name)
    img = Image.open(r"cropped_img/" + name)
    conv_img = img.convert('RGB')
    ls_imgs.append(conv_img)

ls_imgs[0].save(r"result.pdf", save_all=True, append_images=ls_imgs[1:])    

