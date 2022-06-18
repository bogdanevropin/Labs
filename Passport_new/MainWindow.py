from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtWidgets import (
    QWidget, QFrame, QDialog, QInputDialog, QLabel, QPushButton, QHBoxLayout, QVBoxLayout, QGridLayout, 
    QSizePolicy
)
from PyQt5.QtGui import QPixmap, QIcon


from style import style
from datetime import date

WINDOW_TITLE = 'Passport'
WINDOW_ICON = 'data/icon.png'
EXAMPLE_PICTURE = 'data/pass282.jpg'

MIN_WINDOW_WIDTH = 640
MIN_WINDOW_HEIGHT = 320

DATA_FIELDS = ['Surname', 'Name', 'Nationality', 'Date of birth', 'Gender']
today_data = date.today()


class PictureView(QLabel):
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self._pixmap_src = None
        self.setAlignment(Qt.AlignTop)
        
    def load_picture(self, filepath):
        pix = QPixmap(filepath)
        if pix.isNull():
            print('picture "{}" not loaded'.format(filepath))
            return
        
        self._pixmap_src = pix
        self.update_picture(self.size().width(), self.size().height())

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.update_picture(event.size().width(), event.size().height())
    
    def update_picture(self, max_width, max_height):
        if self._pixmap_src is None:
            return
        
        self.setPixmap(self._pixmap_src.scaled(
            max_width, max_height, Qt.KeepAspectRatio
        ))


class DataView(QFrame):
    
    def __init__(self, fields_list, parent=None):
        super().__init__(parent)
        self._fields = {}
        
        self.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        
        layout = QGridLayout()
        layout.setAlignment(Qt.AlignTop)
        self.setLayout(layout)
        
        self._generate_fields_widgets(fields_list)

    def _generate_fields_widgets(self, fields_list):
        for index, field in enumerate(fields_list):
            name_label = QLabel(field + ':')
            value_label = QLabel('-')
            self._fields[field] = value_label

            self.layout().addWidget(name_label, index, 0)
            self.layout().addWidget(value_label, index, 1)

    def set_field_value(self, name, value):
        value_label = self._fields.get(name)
        if value_label is not None:
            value_label.setText(str(value))
        else:
            print('field {} is not exists'.format(name))


class inputDataDialog(QDialog):

    value_changed = pyqtSignal(str, str)  # field name, new value

    def __init__(self, fields_list, parent=None):
        super().__init__(parent)

        # dialog window setting
        self.setWindowTitle('Editing field')
        self.setFixedSize(280, 180)
        self.setWindowIcon(QIcon(WINDOW_ICON))
        self.setModal(True)

        self.setLayout(QVBoxLayout())
        self.layout().setAlignment(Qt.AlignTop)
        self._generate_fields_widgets(fields_list)

    def _generate_fields_widgets(self, fields_list):
        for field in fields_list:
            button = QPushButton(field)
            button.clicked.connect(self.get_input)
            self.layout().addWidget(button)

    def get_input(self):
        selected_button = self.sender()
        field_name = selected_button.text()
        query_text = 'Enter your {}:'.format(field_name)

        text, status = QInputDialog.getText(
            self, 'Input', query_text
        )
        if status:
            self.value_changed.emit(field_name, text)
            # print(''.forfield_name, text)


class MainWindow(QFrame):

    def __init__(self):
        super().__init__()

        # window setting
        self.setWindowTitle(WINDOW_TITLE)
        self.setWindowIcon(QIcon(WINDOW_ICON))
        self.setMinimumSize(MIN_WINDOW_WIDTH, MIN_WINDOW_HEIGHT)

        # picture loading widget
        self.picture_view = PictureView()
        self.picture_view.load_picture(EXAMPLE_PICTURE)

        # data showing widget
        self.data_view = DataView(DATA_FIELDS)

        # open data input dialog
        self.open_input_dialog_button = QPushButton('Input your data')
        self.input_data_dialog = inputDataDialog(
            DATA_FIELDS, parent=self
        )

        # layouts
        data_v_layout = QVBoxLayout()
        data_v_layout.addWidget(self.open_input_dialog_button)
        data_v_layout.addWidget(self.data_view)
        data_v_layout.addStretch()

        main_h_layout = QHBoxLayout()
        main_h_layout.addWidget(self.picture_view, 2)
        main_h_layout.addLayout(data_v_layout, 1)
        self.setLayout(main_h_layout)

        # connect actions
        self.open_input_dialog_button.clicked.connect(
            self.input_data_dialog.show
        )
        self.input_data_dialog.value_changed.connect(
            self.data_view.set_field_value
        )

        self.setStyleSheet(style)
        self.setFixedSize(1388, 820)
        # self.resize(1388, 820)
        