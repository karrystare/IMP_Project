from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QSizePolicy, QMessageBox, QShortcut
from Watermarking import (extract_invisilbeWatermark, extract_visibleWatermark,
                          visibleWatermark_with_Pos, invisibleWatermark_with_Pos)
from PyQt5.QtGui import QPixmap, QKeySequence
from PIL import Image, ImageFont, ImageDraw, ImageQt
class Ui_SecondWindow(object):
    def setupUi(self, SecondWindow):
        SecondWindow.setObjectName("SecondWindow")
        SecondWindow.resize(640, 167)
        SecondWindow.setStyleSheet("background-color: rgb(238, 255, 219);")
        self.centralwidget = QtWidgets.QWidget(SecondWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(64, 40, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(251, 188, 255);\n"
"color: rgb(21, 60, 80);")
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(160, 40, 113, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("background-color: rgb(169, 196, 255);")
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(300, 40, 93, 28))
        self.pushButton.setStyleSheet("background-color: rgb(60, 255, 83);\n"
"color: rgb(170, 85, 255);")
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(140, 90, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: rgb(251, 188, 255);\n"
"color: rgb(21, 60, 80);")
        self.label_2.setObjectName("label_2")
        SecondWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(SecondWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 26))
        self.menubar.setObjectName("menubar")
        SecondWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(SecondWindow)
        self.statusbar.setObjectName("statusbar")
        SecondWindow.setStatusBar(self.statusbar)

        self.shortcut = QtWidgets.QShortcut(QKeySequence('Ctrl+Q'), SecondWindow, SecondWindow.close)

        self.retranslateUi(SecondWindow)
        QtCore.QMetaObject.connectSlotsByName(SecondWindow)

    def retranslateUi(self, SecondWindow):
        _translate = QtCore.QCoreApplication.translate
        SecondWindow.setWindowTitle(_translate("SecondWindow", "MainWindow"))
        self.label.setText(_translate("SecondWindow", "Alpha"))
        self.lineEdit.setText(_translate("SecondWindow", "0.5"))
        self.pushButton.setText(_translate("SecondWindow", "Enter"))
        self.pushButton.setShortcut(_translate("SecondWindow", "Return"))
        self.label_2.setText(_translate("SecondWindow", " 0 <= Alpha <= 1"))


class Ui_ThirdWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 491)
        MainWindow.setStyleSheet("background-color: rgb(238, 255, 219);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 60, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(251, 188, 255);\n"
"color: rgb(21, 60, 80);")
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(160, 60, 113, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("background-color: rgb(169, 196, 255);")
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(130, 120, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: rgb(251, 188, 255);\n"
"color: rgb(21, 60, 80);")
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(420, 160, 93, 28))
        self.pushButton.setStyleSheet("background-color: rgb(60, 255, 83);\n"
"color: rgb(170, 85, 255);")
        self.pushButton.setObjectName("pushButton")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(50, 190, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color: rgb(251, 188, 255);\n"
"color: rgb(21, 60, 80);")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(50, 270, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background-color: rgb(251, 188, 255);\n"
"color: rgb(21, 60, 80);")
        self.label_4.setObjectName("label_4")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(160, 190, 113, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("background-color: rgb(169, 196, 255);")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(160, 280, 113, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setStyleSheet("background-color: rgb(169, 196, 255);")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(50, 340, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("background-color: rgb(251, 188, 255);\n"
"color: rgb(21, 60, 80);")
        self.label_5.setObjectName("label_5")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(160, 350, 113, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setStyleSheet("background-color: rgb(169, 196, 255);")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(30, 410, 391, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("background-color: rgb(251, 188, 255);\n"
"color: rgb(21, 60, 80);")
        self.label_6.setObjectName("label_6")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.shortcut = QtWidgets.QShortcut(QKeySequence('Ctrl+Q'), MainWindow, MainWindow.close)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Alpha"))
        self.lineEdit.setText(_translate("MainWindow", "0.5"))
        self.label_2.setText(_translate("MainWindow", "  0 <= Alpha <= 1"))
        self.pushButton.setText(_translate("MainWindow", "Enter"))
        self.pushButton.setShortcut(_translate("MainWindow", "Return"))
        self.label_3.setText(_translate("MainWindow", "X"))
        self.label_4.setText(_translate("MainWindow", "Y"))
        self.lineEdit_2.setText(_translate("MainWindow", "0"))
        self.lineEdit_3.setText(_translate("MainWindow", "0"))
        self.label_5.setText(_translate("MainWindow", "Ratio"))
        self.lineEdit_4.setText(_translate("MainWindow", "0.2"))
        self.label_6.setText(_translate("MainWindow", " If Ratio <= 0 or Ratio > 1 : Ratio = 0.2 ( Default )"))
class Ui_FourthWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)
        MainWindow.setStyleSheet("background-color: rgb(238, 255, 219);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(420, 150, 93, 28))
        self.pushButton.setStyleSheet("background-color: rgb(60, 255, 83);\n"
"color: rgb(170, 85, 255);")
        self.pushButton.setObjectName("pushButton")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(70, 130, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background-color: rgb(251, 188, 255);\n"
"color: rgb(21, 60, 80);")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(70, 200, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("background-color: rgb(251, 188, 255);\n"
"color: rgb(21, 60, 80);")
        self.label_5.setObjectName("label_5")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(70, 50, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color: rgb(251, 188, 255);\n"
"color: rgb(21, 60, 80);")
        self.label_3.setObjectName("label_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(180, 50, 113, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("background-color: rgb(169, 196, 255);")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(180, 210, 113, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setStyleSheet("background-color: rgb(169, 196, 255);")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(20, 280, 391, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("background-color: rgb(251, 188, 255);\n"
"color: rgb(21, 60, 80);")
        self.label_6.setObjectName("label_6")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(180, 140, 113, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setStyleSheet("background-color: rgb(169, 196, 255);")
        self.lineEdit_3.setObjectName("lineEdit_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.shortcut = QtWidgets.QShortcut(QKeySequence('Ctrl+Q'), MainWindow, MainWindow.close)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Enter"))
        self.pushButton.setShortcut(_translate("MainWindow", "Return"))
        self.label_4.setText(_translate("MainWindow", "Y"))
        self.label_5.setText(_translate("MainWindow", "Ratio"))
        self.label_3.setText(_translate("MainWindow", "X"))
        self.lineEdit_2.setText(_translate("MainWindow", "0"))
        self.lineEdit_4.setText(_translate("MainWindow", "0.2"))
        self.label_6.setText(_translate("MainWindow", " If Ratio <= 0 or Ratio > 1 : Ratio = 0.2 ( Default )"))
        self.lineEdit_3.setText(_translate("MainWindow", "0"))
class Ui_FifthWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 167)
        MainWindow.setStyleSheet("background-color: rgb(238, 255, 219);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(280, 30, 93, 28))
        self.pushButton.setStyleSheet("background-color: rgb(60, 255, 83);\n"
"color: rgb(170, 85, 255);")
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(24, 30, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(251, 188, 255);\n"
"color: rgb(21, 60, 80);")
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(140, 30, 113, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("background-color: rgb(169, 196, 255);")
        self.lineEdit.setObjectName("lineEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.shortcut = QtWidgets.QShortcut(QKeySequence('Ctrl+Q'), MainWindow, MainWindow.close)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Enter"))
        self.pushButton.setShortcut(_translate("MainWindow", "Return"))
        self.label.setText(_translate("MainWindow", "Intensity"))
        self.lineEdit.setText(_translate("MainWindow", "30"))

class Ui_MainWindow(object):
    def open_window2(self):
        self.SecondWindow = QtWidgets.QMainWindow()
        self.ui2 = Ui_SecondWindow()
        self.ui2.setupUi(self.SecondWindow)
        self.ui2.pushButton.clicked.connect(self.extract_visibleWatermark_button)
        self.SecondWindow.show()
    def open_window3(self):
        self.ThirdWindow = QtWidgets.QMainWindow()
        self.ui3 = Ui_ThirdWindow()
        self.ui3.setupUi(self.ThirdWindow)
        self.ui3.pushButton.clicked.connect(self.visibleWatermarked_button)
        self.ThirdWindow.show()
    def open_window4(self):
        self.FourthWindow = QtWidgets.QMainWindow()
        self.ui4 = Ui_FourthWindow()
        self.ui4.setupUi(self.FourthWindow)
        self.ui4.pushButton.clicked.connect(self.invisibleWatermarked_button)
        self.FourthWindow.show()
    def open_window5(self):
        self.FifthWindow = QtWidgets.QMainWindow()
        self.ui5 = Ui_FifthWindow()
        self.ui5.setupUi(self.FifthWindow)
        self.ui5.pushButton.clicked.connect(self.extract_invisibleWatermark_button)
        self.FifthWindow.show()
    def choose_image(self):
        self.imagePath, _ = QFileDialog.getOpenFileName()
        if not self.imagePath:
            if self.imagePathBackUp:
                self.imagePath = self.imagePathBackUp
                #print(self.imagePath)
            else:
                #print("Open Image Again")
                msg = QMessageBox()
                msg.setWindowTitle("Open Warning")
                msg.setText("You need to open an image!")

                x = msg.exec_()
            return
        self.imagePathBackUp = self.imagePath
        #print(self.imagePathBackUp)
        pixmap = QPixmap(self.imagePath)
        self.label_6.setPixmap(pixmap)
        self.label_6.setScaledContents(True)
        self.label_6.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        self.image = Image.open(self.imagePath)
    def choose_watermark(self):
        self.watermarkPath, _ = QFileDialog.getOpenFileName()
        if not self.watermarkPath:
            if self.watermarkPathBackUp:
                self.watermarkPath = self.watermarkPathBackUp
            else:
                #print("Open Image Again")
                msg = QMessageBox()
                msg.setWindowTitle("Open Warning")
                msg.setText("You need to open an image!")

                x = msg.exec_()
            return
        self.watermarkPathBackUp = self.watermarkPath
        self.watermarkedImagePath = None
        self.watermarkedImagePathBackUp = None
        self.watermarkedImage = None
        pixmap = QPixmap(self.watermarkPath)
        self.label_5.setPixmap(pixmap)
        self.label_5.setScaledContents(True)
        self.label_5.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        self.watermark = Image.open(self.watermarkPath)
    def choose_watermarked_Image(self):
        self.watermarkedImagePath, _ = QFileDialog.getOpenFileName()
        if not self.watermarkedImagePath:
            if self.watermarkedImagePathBackUp:
                self.watermarkedImagePath = self.watermarkedImagePathBackUp
            else:
                #print("Open Image Again")
                msg = QMessageBox()
                msg.setWindowTitle("Open Warning")
                msg.setText("You need to open an image!")

                x = msg.exec_()
            return
        self.watermarkedImagePathBackUp = self.watermarkedImagePath
        self.watermarkPath = None
        self.watermarkPathBackUp = None
        self.watermark = None
        pixmap = QPixmap(self.watermarkedImagePath)
        self.label_5.setPixmap(pixmap)
        self.label_5.setScaledContents(True)
        self.label_5.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        self.watermarkedImage = Image.open(self.watermarkedImagePath)
    def visibleWatermarked_button(self):
        if not self.imagePath:
            #print("Need a base image")
            msg = QMessageBox()
            msg.setWindowTitle("Image Warning")
            msg.setText("Do not detect any base image!")

            x = msg.exec_()
            return
        if not self.watermarkPath:
            #print("Need a watermerk image")
            msg = QMessageBox()
            msg.setWindowTitle("watermark Warning")
            msg.setText("Do not detect any watermark image!")

            x = msg.exec_()
            return
        self.alpha = float(self.ui3.lineEdit.text())
        self.X = int(self.ui3.lineEdit_2.text())
        self.Y = int(self.ui3.lineEdit_3.text())
        self.Ratio = float(self.ui3.lineEdit_4.text())
        #print("Done")
        self.visibleOutput= visibleWatermark_with_Pos(self.image,
                    self.watermarkPath, (self.X,self.Y), ratio = self.Ratio, alpha = self.alpha)
        #("Done")
        im = self.visibleOutput.convert(("RGB"))
        data = im.tobytes("raw", "RGB")
        qim = QtGui.QImage(data, im.size[0], im.size[1], QtGui.QImage.Format_RGB888)
        pixmap = QtGui.QPixmap.fromImage(qim)
        self.label.setPixmap(pixmap)
        self.label.setScaledContents(True)
        self.label.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        self.ThirdWindow.close()
    def invisibleWatermarked_button(self):
        if not self.imagePath:
            #print("Need a base image")
            msg = QMessageBox()
            msg.setWindowTitle("Image Warning")
            msg.setText("Do not detect any base image!")

            x = msg.exec_()
            return
        if not self.watermarkPath:
            #print("Need a watermerk image")
            msg = QMessageBox()
            msg.setWindowTitle("watermark Warning")
            msg.setText("Do not detect any watermark image!")

            x = msg.exec_()
            return
        self.X = int(self.ui4.lineEdit_2.text())
        self.Y = int(self.ui4.lineEdit_3.text())
        self.Ratio = float(self.ui4.lineEdit_4.text())
        #print("Done")
        self.invisibleOutput= invisibleWatermark_with_Pos(self.image,
                    self.watermarkPath, (self.X,self.Y), ratio = self.Ratio)
        #print("Done")
        im = self.invisibleOutput.convert(("RGB"))
        data = im.tobytes("raw", "RGB")
        qim = QtGui.QImage(data, im.size[0], im.size[1], QtGui.QImage.Format_RGB888)
        pixmap = QtGui.QPixmap.fromImage(qim)
        self.label_2.setPixmap(pixmap)
        self.label_2.setScaledContents(True)
        self.label_2.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        self.FourthWindow.close()
    def extract_visibleWatermark_button(self):
        if not self.watermarkedImagePath:
            #print("Need to have watermarked image")
            msg = QMessageBox()
            msg.setWindowTitle("Watermarked Image Warning")
            msg.setText("Do not detect any watermarked image!")

            x = msg.exec_()
            return
        if not self.imagePath:
            #print("Need a base image")
            msg = QMessageBox()
            msg.setWindowTitle("Image Warning")
            msg.setText("Do not detect any base image!")

            x = msg.exec_()
            return
        self.alpha = float(self.ui2.lineEdit.text())
        try:
            self.visibleWatermark_image = extract_visibleWatermark(self.image.convert(("RGB")), self.watermarkedImage.convert(("RGB")), self.alpha)
        except:
            #print("Not a watermarked image or wrong base image")
            msg = QMessageBox()
            msg.setWindowTitle("Watermarked Image Warning")
            msg.setText("This is not a watermarked image or wrong base image!")
            x = msg.exec_()
            self.SecondWindow.close()
            return
        im = self.visibleWatermark_image.convert(("RGB"))
        data = im.tobytes("raw", "RGB")
        qim = QtGui.QImage(data, im.size[0], im.size[1], QtGui.QImage.Format_RGB888)
        pixmap = QtGui.QPixmap.fromImage(qim)
        self.label_3.setPixmap(pixmap)
        self.label_3.setScaledContents(True)
        self.label_3.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        self.SecondWindow.close()
    def extract_invisibleWatermark_button(self):
        if not self.watermarkedImagePath:
            #print("Need to have watermarked image")
            msg = QMessageBox()
            msg.setWindowTitle("Watermarked Image Warning")
            msg.setText("Do not detect any watermarked image!")

            x = msg.exec_()
            return
        if not self.imagePath:
            #print("Need a base image")
            msg = QMessageBox()
            msg.setWindowTitle("Image Warning")
            msg.setText("Do not detect any base image!")

            x = msg.exec_()
            return
        self.intensity = float(self.ui5.lineEdit.text())
        try:
            self.invisibleWatermark_image = extract_invisilbeWatermark(self.image.convert(("RGB")), self.watermarkedImage.convert(("RGB")), self.intensity)
        except:
            #print("Not a watermarked image or wrong base image")
            msg = QMessageBox()
            msg.setWindowTitle("Watermarked Image Warning")
            msg.setText("This is not a watermarked image or wrong base image!")
            x = msg.exec_()
            self.SecondWindow.close()
            return
        im = self.invisibleWatermark_image.convert(("RGB"))
        data = im.tobytes("raw", "RGB")
        qim = QtGui.QImage(data, im.size[0], im.size[1], QtGui.QImage.Format_RGB888)
        pixmap = QtGui.QPixmap.fromImage(qim)
        self.label_4.setPixmap(pixmap)
        self.label_4.setScaledContents(True)
        self.label_4.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        self.FifthWindow.close()
    def save_visible_watermarked(self):
        if not self.visibleOutput:
            #print("Need to have output image")
            msg = QMessageBox()
            msg.setWindowTitle("Saving Warning")
            msg.setText("Do not detect any output image!")

            x = msg.exec_()
            return
        # selecting file path
        filePath, _ = QFileDialog.getSaveFileName(MainWindow, "Save Image", "",
                                                  "PNG(*.png);;JPEG(*.jpg *.jpeg);;All Files(*.*) ")

        # if file path is blank return back
        if filePath == "":
            return
        # saving canvas at desired path
        self.visibleOutput.save(filePath)
    def save_invisible_watermarked(self):
        if not self.invisibleOutput:
            #print("Need to have output image")
            msg = QMessageBox()
            msg.setWindowTitle("Saving Warning")
            msg.setText("Do not detect any output image!")

            x = msg.exec_()
            return
        # selecting file path
        filePath, _ = QFileDialog.getSaveFileName(MainWindow, "Save Image", "",
                                                  "PNG(*.png);;JPEG(*.jpg *.jpeg);;All Files(*.*) ")

        # if file path is blank return back
        if filePath == "":
            return
        # saving canvas at desired path
        self.invisibleOutput.save(filePath)
    def save_extracted_visible_watermark(self):
        if not self.visibleWatermark_image:
            #print("Need to have output image")
            msg = QMessageBox()
            msg.setWindowTitle("Saving Warning")
            msg.setText("Do not detect any output image!")

            x = msg.exec_()
            return
        # selecting file path
        filePath, _ = QFileDialog.getSaveFileName(MainWindow, "Save Image", "",
                                                  "PNG(*.png);;JPEG(*.jpg *.jpeg);;All Files(*.*) ")

        # if file path is blank return back
        if filePath == "":
            return
        # saving canvas at desired path
        self.visibleWatermark_image.save(filePath)
    def save_extracted_invisible_watermark(self):
        if not self.invisibleWatermark_image:
            #print("Need to have output image")
            msg = QMessageBox()
            msg.setWindowTitle("Saving Warning")
            msg.setText("Do not detect any output image!")

            x = msg.exec_()
            return
        # selecting file path
        filePath, _ = QFileDialog.getSaveFileName(MainWindow, "Save Image", "",
                                                  "PNG(*.png);;JPEG(*.jpg *.jpeg);;All Files(*.*) ")

        # if file path is blank return back
        if filePath == "":
            return
        # saving canvas at desired path
        self.invisibleWatermark_image.save(filePath)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(949, 753)
        MainWindow.setStyleSheet("background-color: rgb(255, 241, 160);")

        self.image = None
        self.watermark = None
        self.imagePath = None
        self.watermarkedImage = None
        self.watermarkedImagePath = None
        self.watermarkPath = None
        self.imagePathBackUp = None
        self.watermarkPathBackUp = None
        self.watermarkedImagePathBackUp = None
        self.visibleOutput = None
        self.invisibleOutput = None
        self.visibleWatermark_image = None
        self.invisibleWatermark_image = None
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(470, 70, 201, 211))
        self.label.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(700, 70, 201, 211))
        self.label_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(470, 350, 201, 211))
        self.label_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(700, 350, 201, 211))
        self.label_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda : self.choose_image())
        self.pushButton.setGeometry(QtCore.QRect(120, 10, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(0, 170, 255);\n"
"color: rgb(255, 3, 0);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget, clicked = lambda : self.choose_watermark())
        self.pushButton_2.setGeometry(QtCore.QRect(120, 60, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgb(0, 170, 255);\n"
"color: rgb(255, 3, 0);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget, clicked = lambda : self.choose_watermarked_Image())
        self.pushButton_3.setGeometry(QtCore.QRect(90, 110, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("background-color: rgb(0, 170, 255);\n"
"color: rgb(255, 3, 0);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget, clicked = lambda : self.open_window3())
        self.pushButton_4.setGeometry(QtCore.QRect(490, 10, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("background-color: rgb(0, 170, 255);\n"
"color: rgb(255, 3, 0);")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget, clicked = lambda : self.open_window4())
        self.pushButton_5.setGeometry(QtCore.QRect(700, 10, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("background-color: rgb(0, 170, 255);\n"
"color: rgb(255, 3, 0);")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget, clicked = lambda : self.open_window2())
        self.pushButton_6.setGeometry(QtCore.QRect(460, 290, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet("background-color: rgb(0, 170, 255);\n"
"color: rgb(255, 3, 0);")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget, clicked = lambda : self.open_window5())
        self.pushButton_7.setGeometry(QtCore.QRect(700, 290, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setStyleSheet("background-color: rgb(0, 170, 255);\n"
"color: rgb(255, 3, 0);")
        self.pushButton_7.setObjectName("pushButton_7")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(100, 470, 201, 211))
        self.label_5.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(100, 210, 201, 211))
        self.label_6.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(140, 170, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgb(235, 50, 222);\n"
"background-color: rgb(149, 255, 156);")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(60, 430, 321, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color: rgb(235, 50, 222);\n"
"background-color: rgb(149, 255, 156);")
        self.label_8.setObjectName("label_8")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget, clicked = lambda : self.save_visible_watermarked())
        self.pushButton_8.setGeometry(QtCore.QRect(430, 580, 241, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setStyleSheet("background-color: rgb(255, 54, 28);\n"
                                        "color: rgb(70, 64, 255);")
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget, clicked = lambda : self.save_invisible_watermarked())
        self.pushButton_9.setGeometry(QtCore.QRect(680, 580, 251, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setStyleSheet("background-color: rgb(255, 54, 28);\n"
                                        "color: rgb(70, 64, 255);")
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(self.centralwidget, clicked = lambda : self.save_extracted_visible_watermark())
        self.pushButton_10.setGeometry(QtCore.QRect(350, 650, 291, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_10.setFont(font)
        self.pushButton_10.setStyleSheet("background-color: rgb(255, 54, 28);\n"
                                         "color: rgb(70, 64, 255);")
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_11 = QtWidgets.QPushButton(self.centralwidget, clicked = lambda : self.save_extracted_invisible_watermark())
        self.pushButton_11.setGeometry(QtCore.QRect(650, 650, 281, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_11.setFont(font)
        self.pushButton_11.setStyleSheet("background-color: rgb(255, 54, 28);\n"
                                         "color: rgb(70, 64, 255);")
        self.pushButton_11.setObjectName("pushButton_11")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 949, 26))
        self.menubar.setObjectName("menubar")
        self.menuWindow = QtWidgets.QMenu(self.menubar)
        self.menuWindow.setObjectName("menuWindow")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.menuWindow.addAction(self.actionExit)
        self.menubar.addAction(self.menuWindow.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Choose Image"))
        self.pushButton_2.setText(_translate("MainWindow", "Choose Watermark"))
        self.pushButton_3.setText(_translate("MainWindow", "Choose Watermarked Image"))
        self.pushButton_4.setText(_translate("MainWindow", "Visible Watermark"))
        self.pushButton_5.setText(_translate("MainWindow", "Invisible Watermark"))
        self.pushButton_6.setText(_translate("MainWindow", "Extract Visible Watermark"))
        self.pushButton_7.setText(_translate("MainWindow", "Extract Inviisible Watermark"))
        self.label_7.setText(_translate("MainWindow", " Base Image"))
        self.label_8.setText(_translate("MainWindow", "   Watermark Image/Watermarked Image"))
        self.pushButton_8.setText(_translate("MainWindow", "Save Visible Watermark"))
        self.pushButton_8.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.pushButton_9.setText(_translate("MainWindow", "Save Invisible Watermark"))
        self.pushButton_9.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.pushButton_10.setText(_translate("MainWindow", "Save Extracted Visible image"))
        self.pushButton_10.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.pushButton_11.setText(_translate("MainWindow", "Save Extracted Inisible image"))
        self.pushButton_11.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.menuWindow.setTitle(_translate("MainWindow", "WaterImage Window"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionExit.setShortcut(_translate("MainWindow", "Ctrl+Q"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.actionExit.triggered.connect(MainWindow.close)
    MainWindow.show()
    sys.exit(app.exec_())
