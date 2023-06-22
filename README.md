
# Tesseract-Demo

The aim of this project is to build a tool that shows the capabilities of Tesseract. I have built a Qt UI to allow users to tesseract. Do note this is not a completed project, while most functions do work, I still need to add error messages and handle exceptions more often.

## How to setup (Linux-only)

The following prerequisites are required:

```bash
sudo apt install libtesseract-dev
sudo apt install tesseract-ocr
sudo apt install python3-opencv
```

Then we'd also need the following python dependecies:

```bash
pip install pytesseract
pip install PySide6
pip install Pillow
```

## Editing th UI
The GUI is completely editable via the "Demo.ui" file. Inorder to change the ui you need qt designer and then you would need to export the python code and copy it to "DemoUI.py".

Include the following:

```python
from PySide6.QtCore import Qt, Signal
class ImageLabel(QLabel):
    clicked = Signal(int, int)

    def __init__(self, parent=None):
        super().__init__(parent)

    def mousePressEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            position = event.pos()
            self.clicked.emit(position.x(), position.y())
```

Finally change the following line:
```python
self.imgFrame = QLabel(self.centralwidget)
```
to
```python
self.imgFrame = ImageLabel(self.centralwidget)
```

## Output
![alt text](https://github.com/KodinGuy08/Tesseract-Demo/blob/main/images/demo.png?raw=true)
