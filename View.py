# main view

from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QMainWindow, QWidget, QHBoxLayout, QVBoxLayout, QTabWidget, QDialog, QPushButton
from Components import REditorConnector, RStatusBar, RHtmlViewer
from style import * # to Core module import
from Open import ROpenSaveDialog

class RMainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # building tabs
        self.editor = REditorConnector(self)
        self.preview = RHtmlViewer(self)
        
        # building top bar
        self.build_header()

        # building tab view
        self.tabs = QTabWidget()
        self.tabs.addTab(self.editor, "Editor")
        self.tabs.addTab(self.preview, "Preview")
        self.tabs.tabBar().hide()
        
        # building statusbar
        self.statusbar = self.buidl_statusbar()
        self.statusbar.load()
        self.fill_statusbar()
        
        # building layout
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addSpacing(0)
        layout.addWidget(self.header)
        layout.addWidget(self.tabs)
        layout.addWidget(self.statusbar)
        self.setLayout(layout)
        
        # prepare styling
        self.load_fonts()
        self.load_style()
        
        # loading icon
        self.setWindowIcon(QtGui.QIcon('resources/icon.png'))
        
        # building window
        self.setWindowTitle("River")
        self.setMinimumSize(800, 600)
        self.setContentsMargins(0, 0, 0, 0)

        self.show()

    def build_header(self):
        self.header = QWidget(self)
        self.menu_button = self.create_button("⋮", None)
        self.close_button = self.create_button("✖", None)
        layout = QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addSpacing(0)
        layout.addWidget(self.menu_button)
        layout.addStretch()
        layout.addWidget(self.close_button)
        self.header.setLayout(layout)
        
    def create_button(self, caption, on_click_method):
        button = QPushButton(caption)
        button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        if on_click_method != None:
            button.clicked.connect(on_click_method)
        return button

    def buidl_statusbar(self):
        component = RStatusBar()
        component.add_panel("PROJECT")
        component.add_panel("INFO", "C")
        component.add_panel("MESSAGE", "R")
        return component
    
    def fill_statusbar(self):
        self.statusbar.set_content("PROJECT", "Informacja o projekcie")
        self.statusbar.set_content("INFO", "F1 Pomoc  F2 Otworz")
        self.statusbar.set_content("MESSAGE", "")
        
    def load_fonts(self):
        QtGui.QFontDatabase.addApplicationFont("resources/rm-regular.ttf")
        QtGui.QFontDatabase.addApplicationFont("resources/rm-sbold.ttf")
        
    def load_style(self):
        self.setStyleSheet(stylesheet)

    def open_new_action(self, path):
        dialog = ROpenSaveDialog()
        dialog.load_projects(path)

        result = dialog.exec_()
        if result == QDialog.Accepted:
            return dialog.get_values()
        else:
            return None

    
class RMainWindowConnector(RMainWindow):

    def __init__(self):
        super().__init__()
    
    def set_focus(self):
        self.editor.set_focus()

    def is_modified(self):
        return self.editor.is_modified() # or sidepad modified

    def set_project_info(self, name, other = ""):
        data = ">> " + name + " >> "
        self.statusbar.set_content("PROJECT", data)

    def set_unmodified(self):
        self.editor.cool_down()

    def set_main_content(self, content):
        self.editor.set_content(content)

    def get_main_content(self):
        return self.editor.get_content()

    def show_message(self, message):
        self.statusbar.set_content("MESSAGE", message)
