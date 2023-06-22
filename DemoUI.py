# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DemoAAVzKd.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QLabel, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QSpinBox, QVBoxLayout, QWidget)
    
from PySide6.QtCore import Qt, Signal
class ImageLabel(QLabel):
    clicked = Signal(int, int)

    def __init__(self, parent=None):
        super().__init__(parent)

    def mousePressEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            position = event.pos()
            self.clicked.emit(position.x(), position.y())

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(640, 480)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lblAppName = QLabel(self.centralwidget)
        self.lblAppName.setObjectName(u"lblAppName")

        self.verticalLayout.addWidget(self.lblAppName)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalSpacer = QSpacerItem(40, 1, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout_5.addItem(self.horizontalSpacer)

        self.imgFrame = ImageLabel(self.centralwidget)
        self.imgFrame.setObjectName(u"imgFrame")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.imgFrame.sizePolicy().hasHeightForWidth())
        self.imgFrame.setSizePolicy(sizePolicy)
        self.imgFrame.setFrameShape(QFrame.StyledPanel)
        self.imgFrame.setFrameShadow(QFrame.Raised)
        self.imgFrame.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.imgFrame)


        self.horizontalLayout.addLayout(self.verticalLayout_5)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(10, -1, 10, -1)
        self.lblOem = QLabel(self.centralwidget)
        self.lblOem.setObjectName(u"lblOem")

        self.verticalLayout_2.addWidget(self.lblOem)

        self.spnOem = QSpinBox(self.centralwidget)
        self.spnOem.setObjectName(u"spnOem")
        self.spnOem.setMinimum(1)
        self.spnOem.setMaximum(3)

        self.verticalLayout_2.addWidget(self.spnOem)

        self.lblPsm = QLabel(self.centralwidget)
        self.lblPsm.setObjectName(u"lblPsm")

        self.verticalLayout_2.addWidget(self.lblPsm)

        self.spnPsm = QSpinBox(self.centralwidget)
        self.spnPsm.setObjectName(u"spnPsm")
        self.spnPsm.setMaximum(13)
        self.spnPsm.setValue(1)

        self.verticalLayout_2.addWidget(self.spnPsm)

        self.lblSrc = QLabel(self.centralwidget)
        self.lblSrc.setObjectName(u"lblSrc")

        self.verticalLayout_2.addWidget(self.lblSrc)

        self.cmboxSrc = QComboBox(self.centralwidget)
        self.cmboxSrc.addItem("")
        self.cmboxSrc.addItem("")
        self.cmboxSrc.addItem("")
        self.cmboxSrc.setObjectName(u"cmboxSrc")
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.cmboxSrc.sizePolicy().hasHeightForWidth())
        self.cmboxSrc.setSizePolicy(sizePolicy1)

        self.verticalLayout_2.addWidget(self.cmboxSrc)

        self.btnColor = QPushButton(self.centralwidget)
        self.btnColor.setObjectName(u"btnColor")

        self.verticalLayout_2.addWidget(self.btnColor)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.horizontalLayout.addLayout(self.verticalLayout_2)


        self.verticalLayout_6.addLayout(self.horizontalLayout)


        self.verticalLayout.addLayout(self.verticalLayout_6)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btnAction = QPushButton(self.centralwidget)
        self.btnAction.setObjectName(u"btnAction")

        self.horizontalLayout_2.addWidget(self.btnAction)

        self.btnReset = QPushButton(self.centralwidget)
        self.btnReset.setObjectName(u"btnReset")

        self.horizontalLayout_2.addWidget(self.btnReset)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Tesseract Demo", None))
        self.lblAppName.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600;\">Tesseract Demo</span></p></body></html>", None))
        self.imgFrame.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; color:#ef2929;\">No source selected!</span></p></body></html>", None))
        self.lblOem.setText(QCoreApplication.translate("MainWindow", u"OEM", None))
        self.lblPsm.setText(QCoreApplication.translate("MainWindow", u"PSM", None))
        self.lblSrc.setText(QCoreApplication.translate("MainWindow", u"Source", None))
        self.cmboxSrc.setItemText(0, QCoreApplication.translate("MainWindow", u"Local Image", None))
        self.cmboxSrc.setItemText(1, QCoreApplication.translate("MainWindow", u"URL", None))
        self.cmboxSrc.setItemText(2, QCoreApplication.translate("MainWindow", u"Camera", None))

        self.btnColor.setText(QCoreApplication.translate("MainWindow", u"Change Font", None))
        self.btnAction.setText(QCoreApplication.translate("MainWindow", u"Upload", None))
        self.btnReset.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
    # retranslateUi



