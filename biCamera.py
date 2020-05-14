from cap_info import *
import cv2 as cv
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import matplotlib

matplotlib.rcParams['font.sans-serif'] = ['SimHei']
matplotlib.rcParams['font.family'] = 'sans-serif'
matplotlib.rcParams['axes.unicode_minus'] = False

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w = mywindow()
    w.photo_pb.clicked.connect(w.display_img)
    w.show()
    sys.exit(app.exec_())