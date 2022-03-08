from PIL import Image
import sys
import pyocr
import pyocr.builders
import os

pyocr.tesseract.TESSERACT_CMD = os.getenv("TESSERACT_OCR")
# pyocr.tesseract.TESSERACT_CMD = "rC:\Program Files\Tesseract-OCR"
tools = pyocr.get_available_tools()
print("len:", len(tools))
if len(tools) == 0:
    print("no OCR tool found")
    sys.exit(1)
tool = tools[0]
print("Will use tool '%s'" % (tool.get_name()))

langs = tool.get_available_languages()
print("Available languages:%s" % ", ".join(langs))
lang = langs[0]
print("Will use lang '%s'" % (lang))

txt = tool.image_to_string(
    Image.open(r"C:\Users\negot\Pictures\test.png"),
    lang="jpn",
    builder=pyocr.builders.TextBuilder()
)

print(txt)
