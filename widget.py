# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'widget.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import sys
from figures import FigureProcess

class Ui_widget(object):
    def setupUi(self, widget):
        widget.setObjectName("widget")
        widget.resize(800, 480)
        self.gridLayout = QtWidgets.QGridLayout(widget)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_3 = QtWidgets.QPushButton(widget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 0, 4, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(widget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 0, 5, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(widget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 0, 1, 1, 1)
        self.pushButton = QtWidgets.QPushButton(widget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 3, 1, 1)
        self.lcdNumber = QtWidgets.QLCDNumber(widget)
        self.lcdNumber.setObjectName("lcdNumber")
        self.gridLayout.addWidget(self.lcdNumber, 0, 8, 1, 1)

        self.retranslateUi(widget)
        QtCore.QMetaObject.connectSlotsByName(widget)

    def retranslateUi(self, widget):
        _translate = QtCore.QCoreApplication.translate
        widget.setWindowTitle(_translate("widget", "Form"))
        self.pushButton_3.setText(_translate("widget", "PushButton"))
        self.pushButton_4.setText(_translate("widget", "PushButton"))
        self.pushButton_2.setText(_translate("widget", "PushButton"))
        self.pushButton.setText(_translate("widget", "PushButton"))


if __name__ == "__main__":

    class AddFigure(QWidget, Ui_widget):
        def __init__(self):
            super().__init__()
            self.setupUi(self)
            self.setWindowTitle("Display matplotlib")

            self.F = FigureProcess(width=3, height=2, dpi=100)

            self.gridLayout.addWidget(self.F, 1, 1, 1, 8)


    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)
    window = AddFigure()
    window.show()
    sys.exit(app.exec_())