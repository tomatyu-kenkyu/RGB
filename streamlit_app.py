import pytesseract
from PIL import Image

text = pytesseract.image_to_string(Image.open("test.png"), lang="jpn")
print(text)