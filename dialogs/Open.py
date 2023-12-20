from PyQt5.QtWidgets import QDialog, QWidget, QVBoxLayout, QHBoxLayout, QTabWidget, QLabel, QLineEdit, QPushButton, QListWidget, QListWidgetItem, QFormLayout
from PyQt5.QtCore import QEvent
import sys
import os
import re

class RProjectIdentification:
    def __init__(self):
        self.name = ""
        self.author = ""
        self.title = ""
        self.description = ""
        self.new = False

class RProjectItem(QWidget):
    def __init__(self, caption, path):
        super(RProjectItem, self).__init__()
        self.path = path
        self.caption = caption

        layout = QVBoxLayout()
        name_label = QLabel(caption)
        path_label = QLabel(path)
        layout.addWidget(name_label)
        layout.addWidget(path_label)
        self.setLayout(layout)

class ROpenSaveDialog(QDialog):
    def __init__(self):
        super(ROpenSaveDialog, self).__init__()
        self.main_layout = QVBoxLayout()
        self.build_base_window()
        self.build_open_tab()
        self.build_new_tab()
        self.setLayout(self.main_layout)

        self.setMinimumSize(600, 400)
        self.setContentsMargins(0, 0, 0, 0)
        self.setWindowTitle("New/Open project")

        self.selected_project_path = ""
        self.selected_project_name = ""
        self.newly_created = False

    def eventFilter(self, source, event):
        if (event.type() == QEvent.KeyRelease and source is self.name_input):
            name = self.name_input.text()
            code = self.generate_code_name(name)
            self.code_name_input.setText(code)
        return super(ROpenSaveDialog, self).eventFilter(source, event)
    
    def generate_code_name(self, base_name):
        code = base_name.lower()
        code = re.sub(r'[^a-zA-Z0-9]+', '_', code)
        return code
    
    def get_values(self):
        response = RProjectIdentification()
        response.new = self.newly_created

        if response.new:
            response.name = self.code_name_input.text()
            response.title = self.name_input.text()
            response.author = self.author_input.text()
            response.description = self.overview_input.text()
        else:
            response.name = self.selected_project_name
        return response

    def build_base_window(self):
        self.pages = QTabWidget()
        self.pages.currentChanged.connect(self.on_tab_change)
        buttons = QHBoxLayout()
        self.ok_button = QPushButton("OK")
        self.ok_button.clicked.connect(self.on_ok_click)
        self.cancel_button = QPushButton("Cancel")
        self.cancel_button.clicked.connect(self.reject)
        buttons.addStretch()
        buttons.addWidget(self.ok_button)
        buttons.addWidget(self.cancel_button)
        self.main_layout.addWidget(self.pages)
        self.main_layout.addLayout(buttons)
    
    def build_new_tab(self):
        new_tab = QWidget()

        self.name_label = QLabel("Name")
        self.name_input = QLineEdit()
        self.name_input.installEventFilter(self)

        self.author_label = QLabel("Author")
        self.author_input = QLineEdit()

        self.overview_label = QLabel("Short overview")
        self.overview_input = QLineEdit()

        self.code_name_label = QLabel("Codename")
        self.code_name_input = QLabel()

        form_layout = QFormLayout()
        form_layout.addRow(self.name_label, self.name_input)
        form_layout.addRow(self.author_label, self.author_input)
        form_layout.addRow(self.overview_label, self.overview_input)
        form_layout.addRow(self.code_name_label, self.code_name_input)

        new_tab.setLayout(form_layout)

        self.pages.addTab(new_tab, "New")

    def build_open_tab(self):
        open_tab = QWidget()
        open_layout = QVBoxLayout()
        
        self.project_list = QListWidget()
        self.project_list.itemClicked.connect(self.get_selected_project)
        
        open_layout.addWidget(self.project_list)
        open_tab.setLayout(open_layout)
        self.pages.addTab(open_tab, "Open")

    def load_projects(self, directory):
        self.project_list.clear()
        if os.path.isdir(directory):
            for item in os.listdir(directory):
                if not item.startswith(".") and os.path.isdir(os.path.join(directory, item)):

                    sub_directory = os.path.join(directory, item)
                    list_item = QListWidgetItem()

                    item_widget = RProjectItem(item, sub_directory)

                    list_item.setSizeHint(item_widget.sizeHint())
                    self.project_list.addItem(list_item)
                    self.project_list.setItemWidget(list_item, item_widget)

    def get_selected_project(self, item):
        widget = self.project_list.itemWidget(item)
        self.selected_project_path = widget.path
        self.selected_project_name = widget.caption

    def on_tab_change(self, tab):
        if tab == 0:
            self.ok_button.setText("Open")
            self.newly_created = False
        elif tab == 1:
            self.ok_button.setText("Create")
            self.newly_created = True
    
    def on_ok_click(self):
        tab = self.pages.currentIndex()
        isOk = (tab == 0 and self.selected_project_name != "") or (tab == 1 and self.code_name_input.text() != "")
        
        if isOk:
            self.accept()