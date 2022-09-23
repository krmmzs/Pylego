#!/usr/bin python3

import os
from PIL import Image

# https://github.com/madmaze/pytesseract
# https://github.com/tesseract-ocr/tesseract
# https://pypi.org/project/pytesseract/
import pytesseract


def write_file(src, text):
    with open(src, "w") as f:
        f.write(text)


path = os.path.normpath("/home/mouzaisi/MyGit/Pylego/demo/static/1.png")
text = pytesseract.image_to_string(Image.open(path), lang="eng")
write_file("./output.txt", text)
