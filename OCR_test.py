import pytesseract
from pytesseract import Output
import cv2
img = cv2.imread('image.png')

d = pytesseract.image_to_data(img, output_type=Output.DICT)
print(d.keys())

lines = {}

n_boxes = len(d['level'])
for i in range(n_boxes):
    text = d['text'][i]
    if len(text) > 0:
        if d['par_num'][i] in list(lines.keys()):
            lines[d['par_num'][i]] = lines[d['par_num'][i]] + " " + text
        else:
            lines[d['par_num'][i]] = text
        
        (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

print(lines)

cv2.imshow('img', img)
cv2.waitKey(0)
