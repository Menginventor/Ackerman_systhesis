from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import QPainter
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
        main_layout = QHBoxLayout()

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
        #Chassis_drawing = Example()
        #main_layout.addWidget(Chassis_drawing)
        self.Chassis_setup_tab.setLayout(main_layout)


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
