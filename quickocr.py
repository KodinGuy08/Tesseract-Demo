import pytesseract
from pytesseract import Output
import cv2

from PIL import Image

import numpy as np

font = cv2.FONT_HERSHEY_SIMPLEX

scale = 0.8/30

fontScale = 0.8
color = (255, 0, 0)
thickness = 1

def image_resize(image, width = None, height = None, inter = cv2.INTER_AREA):
    # initialize the dimensions of the image to be resized and
    # grab the image size
    dim = None
    (h, w) = image.shape[:2]

    # if both the width and height are None, then return the
    # original image
    if width is None and height is None:
        return image

    # check to see if the width is None
    if width is None:
        # calculate the ratio of the height and construct the
        # dimensions
        r = height / float(h)
        dim = (int(w * r), height)

    # otherwise, the height is None
    else:
        # calculate the ratio of the width and construct the
        # dimensions
        r = width / float(w)
        dim = (width, int(h * r))

    # resize the image
    resized = cv2.resize(image, dim, interpolation = inter)

    # return the resized image
    return resized

def recognize(filename, config=None, color=(255, 0, 0)):
    img = cv2.imread(filename)

    height = img.shape[0]
    width = img.shape[1]

    if width > 1000:
        img = image_resize(img, width=1000, inter = cv2.INTER_AREA)
    
    if height > 600:
        img = image_resize(img, height=600, inter = cv2.INTER_AREA)

    height = img.shape[0]
    width = img.shape[1]

    if config is None:
        d = pytesseract.image_to_data(img, output_type=Output.DICT)
    else:
        d = pytesseract.image_to_data(img, config=config, output_type=Output.DICT)

    lines = {}

    n_boxes = len(d['level'])
    for i in range(n_boxes):
        text = d['text'][i]
        if len(text) > 0:

            image = cv2.putText(img, text,
                                (d['left'][i], d['top'][i]), font, 
                   scale*d['height'][i], color, thickness, cv2.LINE_AA)
            
            if d['par_num'][i] in list(lines.keys()):
                lines[d['par_num'][i]] = lines[d['par_num'][i]] + " " + text
            else:
                lines[d['par_num'][i]] = text

            (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
    
    is_success, im_buf_arr = cv2.imencode(".jpg", img)
    return im_buf_arr.tobytes(), width, height, d
