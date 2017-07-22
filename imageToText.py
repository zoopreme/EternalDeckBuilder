from PIL import Image
import pytesseract
import os
import glob

imgMap = glob.glob("regular/*.png")

tessdata_dir_config = '--tessdata-dir "C:\\Program Files (x86)\\Tesseract-OCR\\tessdata" -c tessedit_char_whitelist=abcdefghijklmnopqrstuvwxyz'

for path in imgMap:
    img = Image.open(path)
    img.load()
    try:
        print pytesseract.image_to_string(img, lang='eng', config=tessdata_dir_config)
    except UnicodeEncodeError:
        print "Error parsing image text"