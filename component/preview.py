
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QListWidget, QListWidgetItem, QVBoxLayout, QPushButton
from PyQt5.QtGui import QBrush, QColor
from PyQt5.QtCore import Qt
from Components import RHtmlViewer

class RPreview(QWidget):

    reload_method = None

    def __init__(self, parent):
        super(RPreview, self).__init__(parent)
        self.setParent(parent)
        self.build_ui()

    def build_ui(self):
        # Left panel
        self.tag_panel = QWidget(self)
        self.tag_panel.setMaximumWidth(300)
        
        self.tag_list = QListWidget(self)
        self.tag_list.itemDoubleClicked.connect(self.tag_select)
        
        deselect_button = QPushButton("Deselect")
        deselect_button.clicked.connect(self.deselect)

        reload_button = QPushButton("Reload")
        reload_button.clicked.connect(self.reload)

        panel_layout = QVBoxLayout()
        panel_layout.addWidget(self.tag_list)
        panel_layout.addWidget(deselect_button)
        panel_layout.addWidget(reload_button)
        self.tag_panel.setLayout(panel_layout)

        # Main screen
        self.html_viewer = RHtmlViewer(self)

        preview_layout = QHBoxLayout()
        preview_layout.addWidget(self.html_viewer)
        preview_layout.addWidget(self.tag_panel)
        self.setLayout(preview_layout)
    
    def deselect(self):
        for index in range(self.tag_list.count()):
            item = self.tag_list.item(index)
            item.setData(Qt.UserRole, False)
            item.setBackground(QColor("#1F1F1F"))
            item.setSelected(False)

    def reload(self):
        selected_tags = []
        for index in range(self.tag_list.count()):
            item = self.tag_list.item(index)
            if item.data(Qt.UserRole):
                selected_tags.append(item.data(1))

        if self.reload_method != None:
            self.reload_method(selected_tags)

    def load_tags(self, dictionary):
        self.tag_list.clear()

        for key, obj in dictionary.dictionary.items():
            item = QListWidgetItem("@" + key)
            item.setData(1, key)
            item.setData(Qt.UserRole, False)
            self.tag_list.addItem(item)
    
    def tag_select(self, item):
        if item.data(Qt.UserRole):
            item.setData(Qt.UserRole, False)
            item.setBackground(QColor("#1E1E1E"))
        else:
            item.setData(Qt.UserRole, True)
            item.setBackground(QColor("#0000FF"))
        item.setSelected(False)

class RPreviewConnector(RPreview):

    def __init__(self, parent):
        super(RPreviewConnector, self).__init__(parent)
    
    def load_build(self, build_file, tags):
        self.html_viewer.load(build_file)
        self.load_tags(tags)