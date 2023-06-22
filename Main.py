import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtWidgets import QMainWindow, QApplication, QPushButton, QFileDialog, QInputDialog, QColorDialog

from PySide6.QtCore import QObject, Qt

from PySide6 import QtGui
from PySide6.QtGui import QPixmap

from DemoUI import Ui_MainWindow as UIWindow

import requests

import os, cv2, Camera

import quickocr as OCR

app = QApplication(sys.argv)

window = QMainWindow()

ui = UIWindow()
ui.setupUi(window)

window.show()

srcIndex = 0
custom_oem_psm_config = r'--oem %d --psm %d'
prev_file = ""
cam = None

color = (255, 0, 0)

ocr_dict = None

def cameraCallback(frame):
    is_success, im_buf_arr = cv2.imencode(".jpg", frame)
    RGBarray = im_buf_arr.tobytes()

    pixmap = QPixmap()

    pixmap.loadFromData(RGBarray)

    ui.imgFrame.setPixmap(pixmap)

def on_combobox_changed(value):
    global srcIndex, cam

    srcIndex = value
    
    print("combobox changed", value)

    try:
        cam.release()
        cam = None
    except:
        ui.btnReset.setEnabled(False)

    if value == 0:
        ui.btnAction.setText("Upload")
        
    if value == 1:
        ui.btnAction.setText("Get text")
        
    if value == 2:
        ui.btnAction.setText("Capture")
        cam = Camera.VideoCapture(0, cameraCallback)
        ui.btnReset.setEnabled(True)
        cam.start()

def computeFromFile(fname=None):
    global prev_file, ocr_dict
    
    if fname is None:
        fname = prev_file

    if len(fname) <= 3:
        return

    prev_file = fname

    config_ = custom_oem_psm_config % (ui.spnOem.value(), ui.spnPsm.value())
    
    RGBarray, width, height, boxes = OCR.recognize(fname, config_, color)

    ocr_dict = boxes

    image = QtGui.QImage(RGBarray, width, height, 3*width, QtGui.QImage.Format_RGB888)
    pixmap = QPixmap()

    pixmap.loadFromData(RGBarray)

    ui.imgFrame.setPixmap(pixmap)

def open_dialog():
    fname = QFileDialog.getOpenFileName(
            window,
            "Open File",
            "${HOME}",
    )

    computeFromFile(fname[0])

def performAction():
    if srcIndex == 0:
        open_dialog()
        
    if srcIndex == 1:
        text, ok = QInputDialog.getText(window, 'Image from URL', 'URL:')

        if ok and len(text) > 5:
            loc = "captured." + text.split(".")[-1]
            
            r = requests.get(text)
            with open(loc, 'wb') as outfile:
                outfile.write(r.content)

            computeFromFile(loc)
            
    if srcIndex == 2:
        frame = cam.read()
        cv2.imwrite("captured.png", frame)
        computeFromFile("captured.png")

        cam.pause()

def performReset():
    if cam is not None:
        cam.start()

def changeConfig():
    computeFromFile()

def changeFontColor():
    global color
    color = QColorDialog.getColor().getRgb()[0:3]
    print(color)

    color = (color[2], color[1], color[0])
    
    computeFromFile()

def showText(mx, my):
    global ocr_dict
    d = ocr_dict
    
    lines = {}

    n_boxes = len(d['level'])
    for i in range(n_boxes):
        text = d['text'][i]
        if len(text) > 0:

            (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])

            if (x < mx) and (mx < x + w):
                if (y < my) and (my < y + h):
                    print(text)
                    break

ui.btnAction.clicked.connect(performAction)
ui.btnReset.clicked.connect(performReset)

ui.imgFrame.clicked.connect(showText)

ui.spnOem.valueChanged.connect(changeConfig)
ui.spnPsm.valueChanged.connect(changeConfig)

ui.cmboxSrc.currentIndexChanged.connect(on_combobox_changed)

ui.btnColor.clicked.connect(changeFontColor)

# Start the event loop.
app.exec_()
