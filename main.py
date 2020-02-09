import sys
from PyQt5 import QtCore, QtWidgets
from mainwindow import Ui_MainWindow
from dialog import Ui_Dialog
from serial_process import SerialProcess
from central_process import *

QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
Dialog = QtWidgets.QDialog()

mainUi = Ui_MainWindow()
mainUi.setupUi(MainWindow)

diaUi = Ui_Dialog()
diaUi.setupUi(Dialog)

sp = SerialProcess()
cp = CentralProcess(mainUi, sp)
p1 = DataProcess2(sp, mainUi)
p1.start()
#p1.join()

MainWindow.show()
#Dialog.show()
sys.exit(app.exec())
