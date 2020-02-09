import sys
from PyQt5 import QtCore, QtWidgets
from mainwindow import Ui_MainWindow
from dialog import Ui_Dialog
from widget import Ui_widget
from serial_process import SerialProcess
from central_process import *
from figures import FigureProcess
import time

QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
app = QtWidgets.QApplication(sys.argv)
MainWindow = MainWindow()
Widget = Widget()


sp = SerialProcess()
p1 = DataProcess(sp)
p1.start()
#time.sleep(1)
fp = FigureProcess(p1)
cp = CentralProcess(MainWindow, Widget, fp, sp)




MainWindow.show()

sys.exit(app.exec())
p1.join()
