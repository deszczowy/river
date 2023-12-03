from PyQt5.QtWidgets import QDialog, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QRadioButton
from Enums import EnPrintSource

class RPrintDialog(QDialog):
    def __init__(self):
        super(RPrintDialog, self).__init__()
        self.build_window()
        self.selected = EnPrintSource.Nothing

        self.setMinimumSize(400, 200)
        self.setContentsMargins(0, 0, 0, 0)
        self.setWindowTitle("Printing")

    def init(self, path, selection):
        self.label.setText(path)
        self.select(selection)

    def build_dialog(self):
        frame = QWidget()
        layout = QVBoxLayout()

        label = QLabel("What to print:")
        self.radio_button_main = QRadioButton('Main text')
        self.radio_button_side = QRadioButton('Side notes')
        self.radio_button_side.setEnabled(False)
        self.radio_button_make = QRadioButton('Compilation')
        self.radio_button_make.setEnabled(False)

        self.radio_button_main.clicked.connect(self.on_select)
        self.radio_button_side.clicked.connect(self.on_select)
        self.radio_button_make.clicked.connect(self.on_select)

        layout.addWidget(label)
        layout.addWidget(self.radio_button_main)
        layout.addWidget(self.radio_button_side)
        layout.addWidget(self.radio_button_make)
        frame.setLayout(layout)
        return frame

    def select(self, which):
        self.selected = which
        if which == EnPrintSource.MainText:
            self.radio_button_main.setChecked(True)
        elif which == EnPrintSource.SideNotes:
            self.radio_button_side.setChecked(True)
        elif which == EnPrintSource.Build:
            self.radio_button_make.setChecked(True)

    def on_select(self):
        if self.radio_button_main.isChecked():
            self.selected = EnPrintSource.MainText
        elif self.radio_button_side.isChecked():
            self.selected = EnPrintSource.SideNotes
        elif self.radio_button_make.isChecked():
            self.selected = EnPrintSource.Build

    def get_value(self):
        return self.selected

    def build_window(self):
        layout = QVBoxLayout()

        buttons = QHBoxLayout()
        self.ok_button = QPushButton("Print")
        self.ok_button.clicked.connect(self.on_print_click)
        self.cancel_button = QPushButton("Cancel")
        self.cancel_button.clicked.connect(self.reject)
        buttons.addStretch()
        buttons.addWidget(self.ok_button)
        buttons.addWidget(self.cancel_button)
        
        self.label = QLabel()

        layout.addWidget(self.build_dialog())
        layout.addWidget(self.label)
        layout.addStretch()
        layout.addLayout(buttons)
        self.setLayout(layout)
    
    def on_print_click(self):
        self.accept()