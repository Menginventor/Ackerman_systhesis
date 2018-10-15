from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtCore import QSettings
import sys
from PyQt5.QtGui import QDoubleValidator
import  time
import pyqtgraph as pg
import pyqtgraph.exporters
import math
import numpy as np
import random
import collections

class main_window(QMainWindow):
    def __init__(self,settings ):
        self.settings = settings
        super(QMainWindow, self).__init__()
        #QMainWindow.__init__(self)
        self.initUI()
    def initUI(self):


        self.setGeometry(300, 300, 500, 600)
        self.setWindowTitle("Ackerman Synthesis")
        self.setWindowIcon(QtGui.QIcon('py_logo.png'))
        self.main_widget = main_widget(self, self.settings)
        self.main_tab_widget = main_tab(self)
        self.setCentralWidget(self.main_tab_widget)
        MainMenu = self.menuBar()
        fileMenu = MainMenu.addMenu('File')

class main_tab(QTabWidget):
    def __init__(self, parent=None):
        super(main_tab, self).__init__(parent)
        self.Chassis_setup_tab = QWidget()
        self.Chassis_setup_tab_UI()
        self.tab2 = QWidget()
        self.tab3 = QWidget()

        self.addTab(self.Chassis_setup_tab, "Chassis Setup")
        self.addTab(self.tab2, "Tab 2")
        self.addTab(self.tab3, "Tab 3")
    def Chassis_setup_tab_UI (self):
        main_layout = QVBoxLayout()

        GB1 = QGroupBox("Wheel Distance")
        layout = QFormLayout()
        LE1 = QLineEdit()
        LE1.setValidator(QDoubleValidator())
        layout.addRow(QLabel("Left to Right Wheel:"), LE1)
        LE2 = QLineEdit()
        LE2.setValidator(QDoubleValidator())
        layout.addRow(QLabel("Front to Rear Wheel:"), LE2)
        LE3 = QLineEdit()
        LE3.setValidator(QDoubleValidator())
        layout.addRow(QLabel("Kingpin distance"), LE3)
        GB1.setLayout(layout)
        main_layout.addWidget(GB1)
        #Chassis_drawing_widget = Chassis_drawing(QColor(0, 0, 0))
        Chassis_drawing_widget = Chassis_drawing()

        main_layout.addWidget(Chassis_drawing_widget)
        self.Chassis_setup_tab.setLayout(main_layout)
class Chassis_drawing(QGraphicsView):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)

        #self.setGeometry(300,300,1280,800)
        self.setFixedSize(600, 600)
        self.scene = QGraphicsScene(self)
        #self.scene.setSceneRect(0, 0, 500, 500)
        self.scene.addLine(0,250,500,250)
        self.scene.addLine(250,0,250,500)
        self.scene.addRect(250,250,5000,5000)

        ####
        self.zoom = 0


        self.photo = QGraphicsPixmapItem()
        self.scene.addItem(self.photo)

        self.setTransformationAnchor(QGraphicsView.AnchorUnderMouse)
        self.setResizeAnchor(QGraphicsView.AnchorUnderMouse)
        #self.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        #self.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.setBackgroundBrush(QtGui.QBrush(QtGui.QColor(127, 127, 127)))
        self.setFrameShape(QFrame.NoFrame)
        ###
        self.setScene(self.scene)
        self.setDragMode(QGraphicsView.ScrollHandDrag)

    def fitInView(self, scale=True):

        #rect = QtCore.QRectF(self.photo.pixmap().rect())
        rect = self.scene.sceneRect()
        print('fitInView')
        print(rect.width(),rect.height())
        if not rect.isNull():
            self.setSceneRect(rect)

            unity = self.transform().mapRect(QtCore.QRectF(0, 0, 1, 1))
            self.scale(1 / unity.width(), 1 / unity.height())
            viewrect = self.viewport().rect()
            scenerect = self.transform().mapRect(rect)
            factor = min(viewrect.width() / scenerect.width(),
                         viewrect.height() / scenerect.height())
            self.scale(factor, factor)
            self.zoom = 0

    def wheelEvent(self, event):

        if event.angleDelta().y() > 0:
            factor = 1.25
            self.zoom += 1
        else:
            factor = 0.8
            self.zoom -= 1
        if self.zoom > 0:
            self.scale(factor, factor)
        elif self.zoom == 0:
            self.fitInView()
        else:
            self.zoom = 0

    def mousePressEvent(self, event):
        if self.photo.isUnderMouse():
            self.photoClicked.emit(QtCore.QPoint(event.pos()))
        super(Chassis_drawing, self).mousePressEvent(event)

class main_widget(QWidget):
    def __init__(self, parent,settings):
        self.settings = settings
        super().__init__(parent)
        self.initUI()
    def initUI(self):
        pass

def main():
    app = QApplication(sys.argv)
    #settings = QSettings('Meng\'s Lab', 'Serial Monitor')
    w = main_window(None)
    w.show()

    sys.exit(app.exec_())



if __name__ == '__main__':
    main()
