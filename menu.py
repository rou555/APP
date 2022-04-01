
import sys
import platform
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

# GUI FILE
from ui_companyinfo import Ui_Form

# IMPORT FUNCTIONS
from ui_functions import *

class MainWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.back_btn.clicked
        ## TOGGLE/BURGUER MENU
        ########################################################################
        self.ui.toggle_btn.clicked.connect(lambda: UIFunctions.toggleMenu(self, 250, True))

        ## PAGES
        ########################################################################

        # PAGE 1
        self.ui.dep_btn.clicked.connect(lambda: self.ui.pages.setCurrentWidget(self.ui.page0))

        # PAGE 2
        self.ui.jd_btn.clicked.connect(lambda: self.ui.pages.setCurrentWidget(self.ui.page1))

        # PAGE 3
        self.ui.att_btn.clicked.connect(lambda: self.ui.pages.setCurrentWidget(self.ui.page2))
        # page 4
        self.ui.acc_btn.clicked.connect(lambda: self.ui.pages.setCurrentWidget(self.ui.page3)) 
       
        ## SHOW ==> MAIN WINDOW
        ########################################################################
        self.show()
        ## ==> END ##

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
