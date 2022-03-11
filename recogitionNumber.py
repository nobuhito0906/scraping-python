from asyncio.windows_events import NULL
import pytesseract
from PIL import Image
import os
import sys
import pyocr
import pyocr.builders

pyocr.tesseract.TESSERACT_CMD = os.getenv("TESSERACT_OCR")

# OCRエンジン取得
tools = pyocr.get_available_tools()
tool = tools[0]

try:
    # 対象ファイルを引数から取得
    ORIGINAL_FILE = sys.argv[1]
    print("filePath:", ORIGINAL_FILE)
except IndexError:
    print("引数が設定されていません。")
    sys.exit(1)

# 画像読み込み
img = Image.open(ORIGINAL_FILE)

# 数値を認識
number = tool.image_to_string(
    img, lang='eng', builder=pyocr.builders.DigitBuilder(tesseract_layout=6))
print("number:", number)
