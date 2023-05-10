# -*- coding: utf-8 -*-
import os
import sys
import subprocess
import json
import paramiko
import datetime
import webbrowser
import threading
import pickle
import nmstore_market_config_rc

from market import * 

if sys.version_info[0] > 2:
    from PyQt5 import uic, QtCore, QtGui, QtWidgets
    from PyQt5.QtWidgets import *
    import _thread
    import winreg
else:
    from PyQt4.QtWidgets import QGridLayout
    from PyQt4.QtGui import *
    from PyQt4 import uic, QtCore, QtGui
    from PyQt4.QtCore import *
    import thread
    import _winreg
    
class XWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = uic.loadUi("C:\\Users\\alswo\\Documents\\test\\resource\\nmstore_mainframe.ui")
        self.setUIEvent()
        self.ui.show()
    
    def setUIEvent(self):
        self.ui.marketconfig.triggered.connect(self.show_marketconfig)
    
    def show_marketconfig(self):
        self.w = marketconfig_main()
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    xwin = XWindow()
    app.exec_()