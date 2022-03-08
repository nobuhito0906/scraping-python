import sys
from PIL import Image
import os

#元画像ディレクトリ
ORIGINAL_FILE_DIR =r"C:\Users\negot\Pictures\medicalBills"+"\\"

#格納先ディレクトリ
TRIMMED_FILE_DIR =r"C:\Users\negot\Pictures\medicalBills\trimmed"+"\\"

#画像パス、左上座標、右下座標を指定してトリミング
def trim(path, left, top, right, bottom):
  im = Image.open(path)
  im_trimmed = im.crop((left,top,right,bottom))
  return im_trimmed

if __name__ == '__main__':
    if os.path.isdir(TRIMMED_FILE_DIR) == False:
        os.makedirs(TRIMMED_FILE_DIR)

    #トリミングする左上の座標
    left,top = 0,50
    #トリミングする右上の座標
    right,bottom =2880,1800

    #画像ファイル名取得
    files = os.listdir(ORIGINAL_FILE_DIR)

    for val in files:
        #オリジナル画像へのパス
        path = ORIGINAL_FILE_DIR +val
        #トリミングされたimageオブジェクトを取得
        im_trimmed=trim(path,left,top,right,bottom)
        #トリミング後のディレクトリに保存
        im_trimmed.save(TRIMMED_FILE_DIR+"cut_"+val,quality=95)
