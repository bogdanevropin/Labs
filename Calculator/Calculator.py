"""
stylish Calculator for everyone
"""
import os
import logging  # logging errors

from PyQt5.QtWidgets import *
from PyQt5 import QtGui

# from PyQt5.QtCore import *
# from PyQt5.QtGui import *
# import re

import operator

from MainWindow import UiMainWindow

# Calculator state.
READY = 0
INPUT = 1


class MainWindow(QMainWindow, UiMainWindow):
    """
    Main window code
    """
    
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        dir_path = os.getcwd()
        self.setWindowIcon(QtGui.QIcon(dir_path + '/Data/Calculator_31111.ico'))
        self.current_op = None
        self.last_operation = None
        self.stack = None
        self.state = None
        
        self.setup_ui(self)

        # Setup numbers
        for n in range(0, 10):
            getattr(self, 'butt_%s' % n).pressed.connect(lambda v=n: self.input_number(v))
        
        # input coma
        getattr(self, 'butt_coma').pressed.connect(lambda v='.': self.input_number(v))
        # Setup operations
        self.butt_plus.pressed.connect(lambda: self.operation(operator.add))
        self.butt_minus.pressed.connect(lambda: self.operation(operator.sub))
        self.butt_multiplying.pressed.connect(lambda: self.operation(operator.mul))
        self.butt_div.pressed.connect(lambda: self.operation(operator.truediv))  # operator.div for Python2.7
        
        self.butt_percent.pressed.connect(self.operation_pc)
        self.butt_equal.pressed.connect(self.equals)
        
        # Setup actions
        self.butt_del.pressed.connect(self.reset)
        self.butt_plus_minus.pressed.connect(self.operation_plus_minus)

        self.actionExit.triggered.connect(self.close)
        
        self.memory = 0
        self.reset()
        
        self.show()
        
    def display(self):
        """
        show expression value
        """
        self.show()

    def reset(self):
        """
        dell all
        """
        self.state = READY
        self.stack = [0]
        self.last_operation = None
        self.current_op = None
        self.expression.setText(f"{self.stack[-1]}")
        self.display()

    def memory_store(self):
        """
        Storing in memory
        """
        self.expression.setText(f"{self.memory}")

    def memory_recall(self):
        """
        recalling from memory
        """
        self.state = INPUT
        self.stack[-1] = self.memory
        self.expression.setText(f"{self.stack[-1]}")
        self.display()

    def input_number(self, v):
        """
        Inputting a number
        :param v:
        """
        if self.state == READY:
            self.state = INPUT
            self.stack[-1] = str(v)
        else:
            self.stack[-1] = str(self.stack[-1]) + str(v)
        
        self.expression.setText(f"{self.stack[-1]}")
        self.display()
    
    def operation_plus_minus(self):
        """
        Changes sign
        """
        self.stack[-1] = str(self.stack[-1])
        if self.stack[-1][0] == '-':
            self.stack[-1] = self.stack[-1][1:]
        else:
            self.stack[-1] = '-' + self.stack[-1]
            
        self.expression.setText(f"{self.stack[-1]}")
        self.display()
    
    def operation(self, op):
        """
        Doing operation
        :param op:
        """
        
        self.stack[-1] = str(self.stack[-1])
        
        if self.stack[-1].replace('-', '', 1).isdigit():
            self.stack[-1] = int(self.stack[-1])
        elif self.stack[-1].replace('.', '', 1).replace('-', '', 1).isdigit():
            self.stack[-1] = float(self.stack[-1])
        
        if self.current_op:  # Complete the current operation
            self.equals()
        
        self.stack.append(0)
        self.state = READY
        self.current_op = op
        
        self.expression.setText(f"{self.stack[-1]}")
        self.display()
    
    def operation_pc(self):
        """
        Operation percent
        """
        self.stack[-1] = str(self.stack[-1])
        
        if self.stack[-1].replace('-', '', 1).isdigit():
            self.stack[-1] = int(self.stack[-1])
        elif self.stack[-1].replace('.', '', 1).replace('-', '', 1).isdigit():
            self.stack[-1] = float(self.stack[-1])
            
        self.stack[-1] = float(self.stack[-1]) * 0.01
        self.expression.setText(f"{round(self.stack[-1], 9)}")
        if round(self.stack[-1], 11) == 0:
            self.stack[-1] = 0
        self.display()
        
        self.display()
    
    def equals(self):
        """
        Equality operation
        """
        # Support to allow '=' to repeat previous operation
        # if no further input has been added.
        if self.state == READY and self.last_operation:
            s, self.current_op = self.last_operation
            self.stack.append(s)
        
        if self.current_op:
            self.last_operation = self.stack[-1], self.current_op
        
            try:
                self.stack[-1] = str(self.stack[-1])
                if self.stack[-1].replace('-', '', 1).isdigit():
                    self.stack[-1] = int(self.stack[-1])
                elif self.stack[-1].replace('.', '', 1).replace('-', '', 1).isdigit():
                    self.stack[-1] = float(self.stack[-1])
                
                self.stack = [self.current_op(*self.stack)]
                
                self.expression.setText(f"{round(self.stack[-1], 9)}")
                if round(self.stack[-1], 11) == 0:
                    self.stack[-1] = 0
                self.display()
                
            except Exception as e:
                logging.exception(e)
                self.stack = [0]
                self.expression.setText(f"Error")
                print(f"Error {e}")
                self.display()
            else:
                self.current_op = None
                self.state = READY
                self.display()


if __name__ == '__main__':
    app = QApplication([])
    app.setApplicationName("Calculon")

    window = MainWindow()
    app.exec_()
