#!/usr/bin python3

import PIL

from PIL import Image
from tkinter.filedialog import *

f1 = askopenfilenames()
# foo = Image.open('path/to/image.jpg')
img = Image.open(f1[0])
# I prefer quality 85 with optimize because the quality isn't affected much, and the file size is much smaller.
img.save("static/Fejg8XBaUAAJs4F.jpeg", "JPEG", optimize=True, quality=85)
Image.open("static/Fejg8XBaUAAJs4F.jpeg")
