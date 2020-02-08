import sys
from PyQt5 import QtCore, QtWidgets
from mainwindow import Ui_MainWindow
from serial_process import SerialProcess
from central_process import CentralProcess

QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()

ui = Ui_MainWindow()
ui.setupUi(MainWindow)

sp = SerialProcess()
cp = CentralProcess(ui, sp)

MainWindow.show()
sys.exit(app.exec())
a = 1