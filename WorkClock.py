# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'WorkClock.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets, QtDesigner
from pygame import mixer
import os

mixer.init()
exec_dir_path = os.path.dirname(os.path.abspath(__file__))


# Model Part
class ClockModel:
    Hours: int
    Minutes: int
    Seconds: int

    def __init__(self, h=0, m=0, s=0):
        self.Hours = h
        self.Minutes = m
        self.Seconds = s

    def StartTimer(self):
        pass

    def StopTimer(self):
        pass

    def IsTimeOver(self):
        pass


# View Part
class Ui_MainWindow(QtWidgets.QMainWindow):

    def mouseMoveEvent(self, e):
        if self.st == 1:
            self.setGeometry(self.x() + e.x() - self.mousePosX, self.y() - self.mousePosY + e.y(), 0, 0)
            print(e.x(), e.y())
            self.resize(310, 210)

    def mouseReleaseEvent(self, e):
        if self.st == 1:
            self.st = 0

    def mousePressEvent(self, e):
        print(dir(e))
        if e.type() == QtCore.QEvent.MouseButtonPress:
            print(e.x())
            print(e.y())
            self.mousePosX = e.x()
            self.mousePosY = e.y()
            self.st = 1

    # def closeEvent(self, event):
    #     print("Close Event")
    #     pass

    def __init__(self):
        super().__init__()
        self.setMouseTracking(True)
        self.Image_src_path = exec_dir_path + '/Images/'
        self.Sound_src_path = exec_dir_path + '/Sounds/'

        self.Timer = QtCore.QTimer()
        self.Timer.timeout.connect(self.DecTimer)
        mixer.music.load(self.Sound_src_path + 'ClockSound.wav')

    def setupUi(self):
        self.setObjectName("MainWindow")
        self.setMouseTracking(True)
        self.setGeometry(250, 250, 0, 0)
        self.resize(310, 210)
        self.setMinimumSize(310, 210)
        self.setMaximumSize(310, 210)
        # Hide frame borders
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.Central_Widget = QtWidgets.QWidget(self)
        self.Central_Widget.setStyleSheet("QWidget{\n"
                                          "background-color: rgb(68, 147, 172);\n"
                                          "border-radius:10px;\n"
                                          "background: url(Images/BackImage1.jpg) no-repeat center;\n"
                                          "}")
        self.Central_Widget.setObjectName("Central_Widget")
        self.Start_btn = QtWidgets.QPushButton(self.Central_Widget)
        self.Start_btn.setGeometry(QtCore.QRect(210, 120, 90, 30))
        font = QtGui.QFont()
        font.setBold(True)
        font.setPointSize(10)
        font.setWeight(75)
        self.Start_btn.setFont(font)
        self.Start_btn.setStyleSheet("QPushButton{\n"
                                     "background: none;\n"
                                     "background-color: rgba(55, 83, 95);\n"
                                     "border-radius:10px;\n"
                                     "border-top-left-radius:20px;\n"
                                     "border-bottom-left-radius:20px;\n"
                                     "color:rgb(155, 236, 226);\n"
                                     "}"
                                     "QPushButton:hover{\n"
                                     "background-color: rgb(75, 93, 105);\n"
                                     "border-radius:10px;\n"
                                     "border-top-left-radius:20px;\n"
                                     "border-bottom-left-radius:20px;\n"
                                     "padding-left: 3px;\n"
                                     "padding-bottom: 3px;\n"
                                     "}")
        self.Start_btn.setObjectName("Start_btn")
        self.Stop_btn = QtWidgets.QPushButton(self.Central_Widget)
        self.Stop_btn.setGeometry(QtCore.QRect(10, 120, 90, 30))
        font = QtGui.QFont()
        font.setBold(True)
        font.setPointSize(10)
        font.setWeight(75)
        self.Stop_btn.setFont(font)
        self.Stop_btn.setAcceptDrops(False)
        self.Stop_btn.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Stop_btn.setAutoFillBackground(False)
        self.Stop_btn.setStyleSheet("QPushButton{\n"
                                    "background: none;\n"
                                    "background-color: rgb(55, 83, 95);\n"
                                    "border-radius:10px;\n"
                                    "border-top-right-radius:20px;\n"
                                    "border-bottom-right-radius:20px;\n"
                                    "color:rgb(155, 236, 226);\n"
                                    "}"
                                    "QPushButton:hover{\n"
                                    "background-color: rgb(75, 93, 105);\n"
                                    "border-radius:10px;\n"
                                    "border-top-right-radius:20px;\n"
                                    "border-bottom-right-radius:20px;\n"
                                    "padding-left: 3px;\n"
                                    "padding-bottom: 3px;\n"
                                    "}")
        self.Stop_btn.setObjectName("Stop_btn")
        self.Config_lbl = QtWidgets.QLabel(self.Central_Widget)
        self.Config_lbl.setGeometry(QtCore.QRect(10, 10, 340, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        font.setItalic(True)
        self.Config_lbl.setFont(font)
        self.Config_lbl.setStyleSheet("QLabel{\n"
                                      "background: none;\n"
                                      "color:rgb(155, 236, 226);\n"
                                      "}")
        self.Config_lbl.setObjectName("Config_lbl")
        self.Cancel_btn = QtWidgets.QPushButton(self.Central_Widget)
        self.Cancel_btn.setGeometry(QtCore.QRect(110, 120, 90, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Cancel_btn.setFont(font)
        self.Cancel_btn.setAcceptDrops(False)
        self.Cancel_btn.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Cancel_btn.setAutoFillBackground(False)
        self.Cancel_btn.setStyleSheet("QPushButton{\n"
                                      "background: none;\n"
                                      "background-color: rgb(55, 83, 95);\n"
                                      "border-radius:10px;\n"
                                      "color:rgb(155, 236, 226);\n"
                                      "}"
                                      "QPushButton:hover{\n"
                                      "background-color: rgb(75, 93, 105);\n"
                                      "border-radius:10px;\n"
                                      "padding-left: 3px;\n"
                                      "padding-bottom: 3px;\n"
                                      "}")

        # Exit Button
        self.Exit_btn = QtWidgets.QPushButton(self.Central_Widget)
        self.Exit_btn.setGeometry(QtCore.QRect(280, 10, 20, 20))
        self.Exit_btn.setAcceptDrops(False)
        self.Exit_btn.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Exit_btn.setStyleSheet("QPushButton{\n"
                                    "background: none;\n"
                                    "background: url(Images/ExitWidget.png) no-repeat center;\n"
                                    "border-radius:10px;\n"
                                    "}"
                                    "QPushButton:hover{\n"
                                    "background-color: rgb(75, 93, 105);\n"
                                    "border-radius:10px;\n"
                                    "padding-left: 3px;\n"
                                    "padding-bottom: 3px;\n"
                                    "}")
        self.Exit_btn.setObjectName("Exit_btn")

        # ClockImage_lbl
        self.ClockImage_lbl = QtWidgets.QLabel(self.Central_Widget)
        self.ClockImage_lbl.setGeometry(QtCore.QRect(125, 10, 35, 30))
        self.Exit_btn.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.ClockImage_lbl.setStyleSheet("QLabel{\n"
                                          "background: none;\n"
                                          "background-image: url(Images/ClockWidget.png) no-repeat center;\n"
                                          "}")
        self.ClockImage_lbl.setObjectName("ClockImage_lbl")

        self.OutputTime_lbl = QtWidgets.QLabel(self.Central_Widget)
        self.OutputTime_lbl.setGeometry(QtCore.QRect(280, 180, 20, 20))
        self.OutputTime_lbl.setText("")
        self.OutputTime_lbl.setObjectName("OutputTime_lbl")
        self.spinBoxHours = QtWidgets.QSpinBox(self.Central_Widget)
        self.spinBoxHours.setGeometry(QtCore.QRect(10, 80, 40, 30))
        self.spinBoxHours.setStyleSheet("QSpinBox{\n"
                                        "background: none;\n"
                                        "color:rgb(155, 236, 226);\n"
                                        "background-color: rgb(55, 83, 95);\n"
                                        "    border-radius:10px;\n"
                                        "}")

        self.spinBoxHours.setWrapping(True)
        self.spinBoxHours.setFrame(False)
        self.spinBoxHours.setAlignment(QtCore.Qt.AlignCenter)
        self.spinBoxHours.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.spinBoxHours.setMaximum(23)
        self.spinBoxHours.setSingleStep(1)
        self.spinBoxHours.setObjectName("spinBoxHours")
        self.spinBoxMinutes = QtWidgets.QSpinBox(self.Central_Widget)
        self.spinBoxMinutes.setGeometry(QtCore.QRect(60, 80, 40, 30))
        self.spinBoxMinutes.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.spinBoxMinutes.setStyleSheet("QSpinBox{\n"
                                          "background: none;\n"
                                          "color:rgb(155, 236, 226);\n"
                                          "background-color: rgb(55, 83, 95);\n"
                                          "    border-radius:10px;\n"
                                          "}")
        self.spinBoxMinutes.setWrapping(True)
        self.spinBoxMinutes.setFrame(False)
        self.spinBoxMinutes.setAlignment(QtCore.Qt.AlignCenter)
        self.spinBoxMinutes.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.spinBoxMinutes.setMaximum(59)
        self.spinBoxMinutes.setSingleStep(1)
        self.spinBoxMinutes.setObjectName("spinBoxMinutes")
        self.spinBoxSeconds = QtWidgets.QSpinBox(self.Central_Widget)
        self.spinBoxSeconds.setGeometry(QtCore.QRect(110, 80, 40, 30))
        self.spinBoxSeconds.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.spinBoxSeconds.setStyleSheet("QSpinBox{\n"
                                          "background: none;\n"
                                          "color:rgb(155, 236, 226);\n"
                                          "background-color: rgb(55, 83, 95);\n"
                                          "    border-radius:10px;\n"
                                          "}")
        self.spinBoxSeconds.setWrapping(True)
        self.spinBoxSeconds.setFrame(False)
        self.spinBoxSeconds.setAlignment(QtCore.Qt.AlignCenter)
        self.spinBoxSeconds.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.spinBoxSeconds.setMaximum(59)
        self.spinBoxSeconds.setSingleStep(1)
        self.spinBoxSeconds.setObjectName("spinBoxSeconds")
        self.Config_lbl_2 = QtWidgets.QLabel(self.Central_Widget)
        self.Config_lbl_2.setGeometry(QtCore.QRect(20, 50, 20, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.Config_lbl_2.setFont(font)
        self.Config_lbl_2.setStyleSheet("QLabel{\n"
                                        "background: none;\n"
                                        "color:rgb(155, 236, 226);\n"
                                        "}")
        self.Config_lbl_2.setObjectName("Config_lbl_2")
        self.Config_lbl_3 = QtWidgets.QLabel(self.Central_Widget)
        self.Config_lbl_3.setGeometry(QtCore.QRect(70, 50, 20, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.Config_lbl_3.setFont(font)
        self.Config_lbl_3.setStyleSheet("QLabel{\n"
                                        "background: none;\n"
                                        "color:rgb(155, 236, 226);\n"
                                        "}")
        self.Config_lbl_3.setObjectName("Config_lbl_3")
        self.Config_lbl_4 = QtWidgets.QLabel(self.Central_Widget)
        self.Config_lbl_4.setGeometry(QtCore.QRect(120, 50, 20, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.Config_lbl_4.setFont(font)
        self.Config_lbl_4.setStyleSheet("QLabel{\n"
                                        "background: none;\n"
                                        "color:rgb(155, 236, 226);\n"
                                        "}")
        self.Config_lbl_4.setObjectName("Config_lbl_4")
        self.setCentralWidget(self.Central_Widget)
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 313, 26))
        self.menubar.setObjectName("menubar")
        self.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

        self.Start_btn.clicked.connect(lambda: self.btn_click_handler(self.Start_btn.objectName()))
        self.Stop_btn.clicked.connect(lambda: self.btn_click_handler(self.Stop_btn.objectName()))
        self.Cancel_btn.clicked.connect(lambda: self.btn_click_handler(self.Cancel_btn.objectName()))
        self.Exit_btn.clicked.connect(lambda: self.btn_click_handler(self.Exit_btn.objectName()))

    # Remake as Service
    def DecTimer(self):
        hours_text = self.spinBoxHours.text()
        minutes_text = self.spinBoxMinutes.text()
        seconds_text = self.spinBoxSeconds.text()
        curr_time = QtCore.QTime()
        curr_time = curr_time.fromString(hours_text + ":" + minutes_text + ":" + seconds_text, "H:m:s")

        if curr_time != QtCore.QTime(0, 0, 0):
            new_time = curr_time.addSecs(-1)
            print(new_time)
            self.spinBoxSeconds.setValue(new_time.second())
            self.spinBoxMinutes.setValue(new_time.minute())
            self.spinBoxHours.setValue(new_time.hour())
        else:
            self.Timer.stop()
            mixer.music.stop()

    # Remake as Service
    def btn_click_handler(self, obj_name):
        print(obj_name)
        if obj_name == "Exit_btn":
            print("Called Exit")
            sys.exit(app.exec_())
        if obj_name == "Start_btn":
            mixer.music.play(-1)
            self.Timer.start(1000)
        elif obj_name == "Stop_btn":
            self.Timer.stop()
            mixer.music.stop()
        else:
            self.Timer.stop()
            mixer.music.stop()
            self.set_all_spinboxes_zero()

    # Remake as Service
    def set_all_spinboxes_zero(self):
        self.spinBoxSeconds.setValue(0)
        self.spinBoxMinutes.setValue(0)
        self.spinBoxHours.setValue(0)
        print("All SpinBoxes set in zero value!")

    # View Part
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "WorkClock"))
        self.Start_btn.setText(_translate("MainWindow", "Start"))
        self.Stop_btn.setText(_translate("MainWindow", "Stop"))
        self.Config_lbl.setText(_translate("MainWindow", "Stopwatch"))
        self.Cancel_btn.setText(_translate("MainWindow", "Cancel"))
        self.Config_lbl_2.setText(_translate("MainWindow", "h:"))
        self.Config_lbl_3.setText(_translate("MainWindow", "m:"))
        self.Config_lbl_4.setText(_translate("MainWindow", "s:"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    #    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi()
    ui.show()
    sys.exit(app.exec_())
