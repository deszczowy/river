from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton

class RMenu(QWidget):
    """
    Component. Main menu.
    Main class for UI building.
    """

    on_new = None
    on_open = None
    on_build = None
    on_print = None
    on_timer = None
    on_fullscreen = None
    on_help = None

    def __init__(self, parent):
        super(RMenu, self).__init__(parent)
        self.max_width = 100
        self.parent = parent
        self.items = []
        self.build_ui()
    
    def build_menu_item(self, caption, on_click_method = None):
        item = self.parent.create_button(caption, on_click_method)
        self.items.append(item)
    
    def build_items(self):
        self.build_menu_item("New", self.action_new)
        self.build_menu_item("Open", self.action_open)
        self.build_menu_item("Build", self.action_build)
        self.build_menu_item("Print", self.action_print)
        self.build_menu_item("Set timer", self.action_timer)
        self.build_menu_item("Fullscreen", self.action_fullscreen)
        self.build_menu_item("Help", self.action_help)
        self.build_menu_item("Quit", self.action_quit)

    def build_ui(self):
        self.setStyleSheet("background-color: gray;")
        self.calculate_and_set_geometry()
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addSpacing(0)
        
        self.build_items()
        for item in self.items:
            layout.addWidget(item)

        layout.addStretch()
        self.setLayout(layout)
        self.hide()

    def resizeEvent(self, event):
        self.calculate_and_set_geometry()

    def calculate_and_set_geometry(self):
        x0 = 0
        y0 = self.parent.header.height()
        x1 = self.max_width
        y1 = self.parent.tabs.height()
        self.setGeometry(x0, y0, x1, y1)

    def action_new(self):
        if self.on_new != None:
            self.on_new()
        self.hide()

    def action_open(self):
        if self.on_open != None:
            self.on_open()
        self.hide()
    
    def action_build(self):
        if self.on_build != None:
            self.on_build()
        self.hide()
    
    def action_print(self):
        if self.on_print != None:
            self.on_print()
        self.hide()

    def action_timer(self):
        if self.on_timer != None:
            self.on_timer()
        self.hide()
    
    def action_fullscreen(self):
        if self.on_fullscreen != None:
            self.on_fullscreen()
        self.hide()

    def action_help(self):
        if self.on_help != None:
            self.on_help()
        self.hide()
    
    def action_quit(self):
        self.parent.close()

class RMenuConnector(RMenu):
    """
    Connector. Interaction with menu component.
    """

    def __init__(self, parent):
        super(RMenuConnector, self).__init__(parent)
