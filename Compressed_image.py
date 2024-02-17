from PIL import image
from tkinter.filedialog import *

file_path = askopenfilename()
img = image.open(file_path)
myheight,mywidth = img.size

img= img.resize((myheight,mywidth),Image.ANTIALIAS)

save_path = asksaveasfilename()
img.save(save_path+"compressed.JPG")
