"""
Make passport for
Patrick Bateman
He is waiting
"""
import logging  # logging errors
import os
from PyQt5.QtWidgets import *
from PyQt5 import QtGui

# from PyQt5.QtCore import *
# from PyQt5.QtGui import *
# import re

import operator

from MainWindow import Ui_main_window, Dialog


class MainWindow(QMainWindow, Ui_main_window):
    """
    Main window code
    """
    
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        dir_path = os.getcwd()
        self.setWindowIcon(QtGui.QIcon(dir_path + '/data/icon.png'))
        
        self.setup_ui(self)
        
        self.show()
    
    def display(self):
        """
        show changes
        """
        self.show()


if __name__ == '__main__':
    app = QApplication([])
    app.setApplicationName("Passport")
    
    passport = MainWindow()
    dialog = Dialog()
    
    app.exec_()
    