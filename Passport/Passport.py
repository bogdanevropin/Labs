"""
Running Passport
"""
import logging  # logging errors
import os
from PyQt5.QtWidgets import *
from PyQt5 import QtGui

# from PyQt5.QtCore import *
# from PyQt5.QtGui import *
# import re

import operator

from MainWindow import Ui_main_window


class MainWindow(QMainWindow, Ui_main_window):
    """
    Main window code
    """
    
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        dir_path = os.getcwd()
        self.setWindowIcon(QtGui.QIcon(dir_path + '/data/icon.png'))
        self.current_op = None
        self.last_operation = None
        self.stack = None
        self.state = None
        
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

    window = MainWindow()
    app.exec_()
    