#!/usr/bin python3

from PIL import Image

# https://github.com/madmaze/pytesseract
# https://github.com/tesseract-ocr/tesseract
# https://pypi.org/project/pytesseract/
import pytesseract

text = pytesseract.image_to_string(
    Image.open("static/2022-09-23_14-31.png"), lang="eng"
)


print(text)
