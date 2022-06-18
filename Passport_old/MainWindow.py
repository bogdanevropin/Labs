"""
Sample windows
"""

import os
from PyQt5 import QtGui, QtCore, QtWidgets


class Dialog(QtWidgets.QWidget):
    
    def __init__(self):
        super().__init__()
    
        self.initUI()
    
    def initUI(self):
        
        self.btn_surname = QtWidgets.QPushButton('Input Surname', self)
        self.btn_surname.move(10, 20)
        self.btn_surname.clicked.connect(self.btn_surname_Dialog)
        
        self.btn_name = QtWidgets.QPushButton('Input Name', self)
        self.btn_name.move(10, 50)
        self.btn_name.clicked.connect(self.btn_name_Dialog)
        
        self.btn_nation = QtWidgets.QPushButton('Input Nationality', self)
        self.btn_nation.move(10, 80)
        self.btn_nation.clicked.connect(self.btn_nation_Dialog)
        
        self.btn_birth = QtWidgets.QPushButton('Input Date of birth', self)
        self.btn_birth.move(10, 110)
        self.btn_birth.clicked.connect(self.btn_birth_Dialog)
        
        self.btn_gender = QtWidgets.QPushButton('Input your GENDER', self)
        self.btn_gender.move(10, 140)
        self.btn_gender.clicked.connect(self.btn_gender_Dialog)
        
        self.setGeometry(50, 50, 200, 190)
        self.setWindowTitle('DATA')
        
        self.show()
    
    def btn_surname_Dialog(self):
        text, ok = QtWidgets.QInputDialog.getText(self, 'Input',
            'Enter your Surname:')
        if ok:
            self.le.setText(str(text))
    
    def btn_name_Dialog(self):
        text, ok = QtWidgets.QInputDialog.getText(self, 'Input',
            'Enter your Name:')
        if ok:
            self.le.setText(str(text))
    
    def btn_nation_Dialog(self):
        text, ok = QtWidgets.QInputDialog.getText(self, 'Input',
            'Enter your NATIONALITY:')
        if ok:
            self.le.setText(str(text))
    
    def btn_birth_Dialog(self):
        text, ok = QtWidgets.QInputDialog.getText(self, 'Input',
            'Enter your Date of birth:')
        if ok:
            self.le.setText(str(text))
    
    def btn_gender_Dialog(self):
        text, ok = QtWidgets.QInputDialog.getText(self, 'Input',
            'Enter your GENDER:')
        if ok:
            self.le.setText(str(text))


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
        MainWindow.resize(1000, 800)
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
        
        # label
        name_label = QtWidgets.QLabel(self.central_widget)
        name_label.setGeometry(QtCore.QRect(0, 0, 400, 100))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(32)
        name_label.setFont(font)
        name_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        name_label.setStyleSheet("color: rgb(32, 32, 32);\n"
                                      "background-color: rgb(255, 255, 255);")
        name_label.setTextFormat(QtCore.Qt.AutoText)
        name_label.setIndent(-2)
        name_label.setObjectName(f"Name")
        name_label.setAlignment(QtCore.Qt.AlignBottom and QtCore.Qt.AlignRight)
        name_label.raise_()
        
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
        self.expression.setGeometry(QtCore.QRect(10, 10, 300, 300))
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
