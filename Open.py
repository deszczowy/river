from PyQt5.QtWidgets import QDialog, QWidget, QVBoxLayout, QHBoxLayout, QTabWidget, QLabel, QPushButton, QListWidget, QListWidgetItem
import sys
import os

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
        super().__init__()
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
    
    def get_values(self):
        name = self.selected_project_name
        path = self.selected_project_path
        crea = self.newly_created
        return name, path, crea

    def build_base_window(self):
        self.pages = QTabWidget()
        self.pages.currentChanged.connect(self.on_tab_change)
        buttons = QHBoxLayout()
        self.ok_button = QPushButton("OK")
        self.ok_button.clicked.connect(self.accept)
        self.cancel_button = QPushButton("Cancel")
        self.cancel_button.clicked.connect(self.reject)
        buttons.addStretch()
        buttons.addWidget(self.ok_button)
        buttons.addWidget(self.cancel_button)
        self.main_layout.addWidget(self.pages)
        self.main_layout.addLayout(buttons)
    
    def build_new_tab(self):
        new_tab = QWidget()
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
                if os.path.isdir(os.path.join(directory, item)):

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

    def get_values(self):
        path = self.selected_project_path
        name = self.selected_project_name
        isNew = self.newly_created
        return path, name, isNew

    def on_tab_change(self, tab):
        if tab == 0:
            self.ok_button.setText("Open")
            self.newly_created = False
        elif tab == 1:
            self.ok_button.setText("Create")
            self.newly_created = True