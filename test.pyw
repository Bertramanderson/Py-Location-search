import sys
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWebEngineWidgets import QWebEngineView


app = QtWidgets.QApplication(sys.argv)
w = QWebEngineView()
w.resize(1000, 900)
w.load(QtCore.QUrl('http://localhost:5173'))
w.setWindowFlags(w.windowFlags() | QtCore.Qt.WindowStaysOnTopHint)
w.show()
app.exec()