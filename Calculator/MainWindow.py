"""
Sample windows
"""

from PyQt5 import QtCore, QtGui, QtWidgets


class UiMainWindow(object):
    """
    Main window
    """

    def setup_ui(self, MainWindow):
        """
        Setup ui of main window
        :param MainWindow:
        """
        MainWindow.setObjectName("Calculator")
        MainWindow.setFixedSize(400, 600)
        
        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        
        MainWindow.setSizePolicy(size_policy)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Triangular)
        
        # central_widget
        self.central_widget = QtWidgets.QWidget(MainWindow)
        self.central_widget.setObjectName("central_widget")
        # top tools
        self.butt_del = QtWidgets.QPushButton(self.central_widget)
        self.butt_plus_minus = QtWidgets.QPushButton(self.central_widget)
        self.butt_percent = QtWidgets.QPushButton(self.central_widget)
        # mid right
        self.butt_div = QtWidgets.QPushButton(self.central_widget)
        self.butt_multiplying = QtWidgets.QPushButton(self.central_widget)
        self.butt_minus = QtWidgets.QPushButton(self.central_widget)
        self.butt_plus = QtWidgets.QPushButton(self.central_widget)
        self.butt_equal = QtWidgets.QPushButton(self.central_widget)
        # numbers
        self.butt_9 = QtWidgets.QPushButton(self.central_widget)
        self.butt_8 = QtWidgets.QPushButton(self.central_widget)
        self.butt_7 = QtWidgets.QPushButton(self.central_widget)
        self.butt_6 = QtWidgets.QPushButton(self.central_widget)
        self.butt_5 = QtWidgets.QPushButton(self.central_widget)
        self.butt_4 = QtWidgets.QPushButton(self.central_widget)
        self.butt_3 = QtWidgets.QPushButton(self.central_widget)
        self.butt_2 = QtWidgets.QPushButton(self.central_widget)
        self.butt_1 = QtWidgets.QPushButton(self.central_widget)
        self.butt_0 = QtWidgets.QPushButton(self.central_widget)
        self.butt_coma = QtWidgets.QPushButton(self.central_widget)
        
        # expression
        self.expression = QtWidgets.QLabel(self.central_widget)
        
        # butt del
        self.butt_del.setGeometry(QtCore.QRect(0, 100, 100, 100))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(22)
        self.butt_del.setFont(font)
        self.butt_del.setStyleSheet("background-color: rgb(198, 197, 202);\n"
                                    "color: rgb(86, 87, 89);")
        self.butt_del.setObjectName("Butt_del")
        
        # butt plus minus
        self.butt_plus_minus.setGeometry(QtCore.QRect(100, 100, 100, 100))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(22)
        self.butt_plus_minus.setFont(font)
        self.butt_plus_minus.setStyleSheet("background-color: rgb(198, 197, 202);\n"
                                           "color: rgb(65, 66, 68);")
        self.butt_plus_minus.setObjectName("Butt_plus_minus")
        
        # butt percent
        self.butt_percent.setGeometry(QtCore.QRect(200, 100, 100, 100))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(22)
        self.butt_percent.setFont(font)
        self.butt_percent.setStyleSheet("background-color: rgb(198, 197, 202);\n"
                                        "color: rgb(72, 73, 75);")
        self.butt_percent.setText("%")
        self.butt_percent.setObjectName("Butt_percent")
        
        # butt division
        self.butt_div.setGeometry(QtCore.QRect(300, 100, 100, 100))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(24)
        self.butt_div.setFont(font)
        self.butt_div.setStyleSheet("background-color: rgb(250, 142, 18);\n"
                                    "color: rgb(255, 238, 178);")
        self.butt_div.setText("/")
        self.butt_div.setObjectName("Butt_division")
        
        # butt multiplying
        self.butt_multiplying.setGeometry(QtCore.QRect(300, 200, 100, 100))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(24)
        font.setWeight(50)
        self.butt_multiplying.setFont(font)
        self.butt_multiplying.setStyleSheet("background-color: rgb(250, 142, 18);\n"
                                            "color: rgb(255, 240, 187);")
        self.butt_multiplying.setText("*")
        self.butt_multiplying.setObjectName("Butt_multiplying")
        
        # butt minus
        self.butt_minus.setGeometry(QtCore.QRect(300, 300, 100, 100))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(24)
        font.setWeight(50)
        self.butt_minus.setFont(font)
        self.butt_minus.setStyleSheet("background-color: rgb(250, 142, 18);\n"
                                      "color: rgb(255, 235, 177);")
        self.butt_minus.setText("-")
        self.butt_minus.setObjectName("Butt_minus")
        
        # butt plus
        self.butt_plus.setGeometry(QtCore.QRect(300, 400, 100, 100))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(24)
        font.setWeight(50)
        self.butt_plus.setFont(font)
        self.butt_plus.setStyleSheet("background-color: rgb(250, 142, 18);\n"
                                     "color: rgb(255, 235, 177);")
        self.butt_plus.setText("+")
        self.butt_plus.setObjectName("Butt_plus")
        
        # butt equal (evaluate)
        self.butt_equal.setGeometry(QtCore.QRect(300, 500, 100, 100))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(24)
        font.setWeight(50)
        self.butt_equal.setFont(font)
        self.butt_equal.setStyleSheet("background-color: rgb(250, 142, 18);\n"
                                      "color: rgb(255, 235, 177);")
        self.butt_equal.setObjectName("Butt_equal")
        
        # Number butts
        # butt 1
        self.butt_1.setGeometry(QtCore.QRect(0, 200, 100, 100))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(22)
        self.butt_1.setFont(font)
        self.butt_1.setStyleSheet("background-color: rgb(210, 211, 215);\n"
                                  "color: rgb(13, 14, 16);")
        self.butt_1.setText("1")
        self.butt_1.setObjectName("Butt_1")
        
        # butt 2
        self.butt_2.setGeometry(QtCore.QRect(100, 200, 100, 100))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(22)
        self.butt_2.setFont(font)
        self.butt_2.setStyleSheet("background-color: rgb(210, 211, 215);\n"
                                  "color: rgb(13, 14, 16);")
        self.butt_2.setText("2")
        self.butt_2.setObjectName("Butt_2")
        
        # butt 3
        self.butt_3.setGeometry(QtCore.QRect(200, 200, 100, 100))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(22)
        self.butt_3.setFont(font)
        self.butt_3.setStyleSheet("background-color: rgb(210, 211, 215);\n"
                                  "color: rgb(13, 14, 16);")
        self.butt_3.setText("3")
        self.butt_3.setObjectName("Butt_3")
        
        # butt 4
        self.butt_4.setGeometry(QtCore.QRect(0, 300, 100, 100))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(22)
        self.butt_4.setFont(font)
        self.butt_4.setStyleSheet("background-color: rgb(210, 211, 215);\n"
                                  "color: rgb(13, 14, 16);")
        self.butt_4.setText("4")
        self.butt_4.setObjectName("Butt_4")
        
        # butt 5
        self.butt_5.setGeometry(QtCore.QRect(100, 300, 100, 100))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(22)
        self.butt_5.setFont(font)
        self.butt_5.setStyleSheet("background-color: rgb(210, 211, 215);\n"
                                  "color: rgb(13, 14, 16);")
        self.butt_5.setText("5")
        self.butt_5.setObjectName("Butt_5")
        
        # butt 6
        self.butt_6.setGeometry(QtCore.QRect(200, 300, 100, 100))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(22)
        self.butt_6.setFont(font)
        self.butt_6.setStyleSheet("background-color: rgb(210, 211, 215);\n"
                                "color: rgb(13, 14, 16);")
        self.butt_6.setText("6")
        self.butt_6.setObjectName("Butt_6")
        
        # butt 7
        self.butt_7.setGeometry(QtCore.QRect(0, 400, 100, 100))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(22)
        self.butt_7.setFont(font)
        self.butt_7.setStyleSheet("background-color: rgb(210, 211, 215);\n"
                                  "color: rgb(13, 14, 16);")
        self.butt_7.setText("7")
        self.butt_7.setObjectName("Butt_7")
        
        # butt 8
        self.butt_8.setGeometry(QtCore.QRect(100, 400, 100, 100))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(22)
        self.butt_8.setFont(font)
        self.butt_8.setStyleSheet("background-color: rgb(210, 211, 215);\n"
                                  "color: rgb(13, 14, 16);")
        self.butt_8.setText("8")
        self.butt_8.setObjectName("Butt_8")
        
        # butt 9
        self.butt_9.setGeometry(QtCore.QRect(200, 400, 100, 100))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(22)
        self.butt_9.setFont(font)
        self.butt_9.setStyleSheet("background-color: rgb(210, 211, 215);\n"
                                  "color: rgb(13, 14, 16);")
        self.butt_9.setText("9")
        self.butt_9.setObjectName("Butt_9")
       
        # butt 0
        self.butt_0.setGeometry(QtCore.QRect(0, 500, 200, 100))
        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.butt_0.sizePolicy().hasHeightForWidth())
        self.butt_0.setSizePolicy(size_policy)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(22)
        self.butt_0.setFont(font)
        self.butt_0.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.butt_0.setStyleSheet("background-color: rgb(210, 211, 215);\n"
                                  "color: rgb(13, 14, 16);")
        self.butt_0.setText("0")
        self.butt_0.setObjectName("Butt_0")
        
        # butt coma
        self.butt_coma.setGeometry(QtCore.QRect(200, 500, 100, 100))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(22)
        self.butt_coma.setFont(font)
        self.butt_coma.setStyleSheet("background-color: rgb(210, 211, 215);\n"
                                     "color: rgb(13, 14, 16);")
        self.butt_coma.setText(".")
        self.butt_coma.setObjectName("Butt_coma")
        
        # label expression
        self.expression.setGeometry(QtCore.QRect(0, 0, 400, 100))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(48)
        self.expression.setFont(font)
        self.expression.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.expression.setStyleSheet("color: rgb(198, 198, 198);\n"
                                      "background-color: rgb(32, 32, 32);")
        self.expression.setTextFormat(QtCore.Qt.AutoText)
        self.expression.setIndent(-2)
        self.expression.setObjectName(f"Expression")
        self.expression.setAlignment(QtCore.Qt.AlignBottom and QtCore.Qt.AlignRight)
        # self.expression.setAlignment(QtCore.Qt.AlignRight)
        # self.expression.setAlignment(QtCore.Qt.AlignVCenter)

        # exit
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        
        # rising all
        self.butt_del.raise_()
        self.butt_plus_minus.raise_()
        self.butt_percent.raise_()
        # mid right
        self.butt_div.raise_()
        self.butt_multiplying.raise_()
        self.butt_minus.raise_()
        self.butt_plus.raise_()
        self.butt_equal.raise_()
        # numbers
        self.butt_9.raise_()
        self.butt_8.raise_()
        self.butt_7.raise_()
        self.butt_6.raise_()
        self.butt_5.raise_()
        self.butt_4.raise_()
        self.butt_3.raise_()
        self.butt_2.raise_()
        self.butt_1.raise_()
        self.butt_0.raise_()
        self.butt_coma.raise_()
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
        MainWindow.setWindowTitle(_translate("Calculator", "Calculator"))
        
        self.butt_del.setText(_translate("MainWindow", "C"))
        self.butt_plus_minus.setText(_translate("MainWindow", "±"))
        self.butt_percent.setText(_translate("MainWindow", "%"))
        # mid right
        self.butt_div.setText(_translate("MainWindow", "÷"))
        self.butt_multiplying.setText(_translate("MainWindow", "×"))
        self.butt_minus.setText(_translate("MainWindow", "-"))
        self.butt_plus.setText(_translate("MainWindow", "+"))
        self.butt_equal.setText(_translate("MainWindow", "="))
        # numbers
        self.butt_9.setText(_translate("MainWindow", "9"))
        self.butt_8.setText(_translate("MainWindow", "8"))
        self.butt_7.setText(_translate("MainWindow", "7"))
        self.butt_6.setText(_translate("MainWindow", "6"))
        self.butt_5.setText(_translate("MainWindow", "5"))
        self.butt_4.setText(_translate("MainWindow", "4"))
        self.butt_3.setText(_translate("MainWindow", "3"))
        self.butt_2.setText(_translate("MainWindow", "2"))
        self.butt_1.setText(_translate("MainWindow", "1"))
        self.butt_0.setText(_translate("MainWindow", "0"))
        self.butt_coma.setText(_translate("MainWindow", ","))
        # expression
        self.expression.setText(_translate("MainWindow", "0"))
