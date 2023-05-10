import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
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

import nmstore_market_refresh_rc
import nmstore_market_add_rc
    
class marketconfig_main(QMainWindow) :
    def __init__(self) :
        QMainWindow.__init__(self)
        self.ui = uic.loadUi("C:\\Users\\alswo\\Documents\\test\\resource\\market\\nmstore_market_main.ui")
        self.ui.show()


if __name__ == "__main__" :
    app = QApplication(sys.argv) 
    myWindow = marketconfig_main() 
    myWindow.show()
    app.exec_()