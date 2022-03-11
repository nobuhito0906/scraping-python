import cv2
import os

# 画像の色を変更する


# 対象の画像
img = cv2.imread("C:\\Users\\negot\\Pictures\\medicalBills\\changed\\edit.png")

# 格納先ディレクトリ
TRIMMED_FILE_DIR = "C:\\Users\\negot\\Pictures\\medicalBills\\changed"+"\\"

if os.path.isdir(TRIMMED_FILE_DIR) == False:
    os.makedirs(TRIMMED_FILE_DIR)
    
h, w, c = img.shape
height = h
width = w
for x in range(37):
    print("x:", x)
    for y in range(50):
        print("y:", y)

        b, g, r = img[x, y]
        print(b, g, r)
        if b < 20 & g < 20:
            img[x, y] = 255, 255, 255

# print(TRIMMED_FILE_DIR+'edit.png')
# cv2.imwrite(TRIMMED_FILE_DIR+'edit.png', img)
