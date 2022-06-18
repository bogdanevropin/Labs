"""
Sample window
"""

import os
from PyQt5 import QtGui, QtCore, QtWidgets


class Ui_main_window(object):
    """
    Main window
    """

    def setup_ui(self, MainWindow):
        """
        Setup ui of main window
        :param MainWindow:
        """

        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        MainWindow.setSizePolicy(size_policy)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Triangular)

        MainWindow.setObjectName("Passport")
        MainWindow.resize(1600, 820)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        
        MainWindow.setSizePolicy(size_policy)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Triangular)
        
        # central_widget
        self.central_widget = QtWidgets.QWidget(MainWindow)
        dir_path = os.getcwd()
        self.central_widget.setWindowIcon(QtGui.QIcon(dir_path + '/data/icon.png'))
        self.central_widget.setObjectName("central_widget")
        
        # expression
        self.expression = QtWidgets.QLabel(self.central_widget)

        h_box = QtWidgets.QHBoxLayout(self.central_widget)
        pixmap = QtGui.QPixmap(dir_path + '/data/pass282.jpg')
        lbl = QtWidgets.QLabel(self.central_widget)
        lbl.setPixmap(pixmap)
        h_box.addWidget(lbl)
        self.central_widget.setLayout(h_box)

        self.central_widget.setWindowTitle('Passport')
        # label expression
        self.expression.setGeometry(QtCore.QRect(0, 0, 300, 300))
        # font = QtGui.QFont()
        # font.setFamily("Calibri")
        # font.setPointSize(48)
        # self.expression.setFont(font)
        # self.expression.setLayoutDirection(QtCore.Qt.LeftToRight)
        # self.expression.setTextFormat(QtCore.Qt.AutoText)
        # self.expression.setIndent(-2)
        self.expression.setObjectName(f"Passport")
        self.expression.setAlignment(QtCore.Qt.AlignBottom and QtCore.Qt.AlignRight)
        # self.expression.setAlignment(QtCore.Qt.AlignRight)
        # self.expression.setAlignment(QtCore.Qt.AlignVCenter)
        
        # exit
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        
        # expression
        self.expression.raise_()

        MainWindow.setCentralWidget(self.central_widget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    
    
    def retranslateUi(self, MainWindow):
        """
        make
        :param MainWindow:
        """
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("Passport", "Passport"))

