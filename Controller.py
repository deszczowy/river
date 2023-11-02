from Core import RProject, RConfig, RTimer, EnProjectFile
from PyQt5.QtWidgets import QShortcut
from PyQt5.QtGui import QKeySequence

class RController:
    def __init__(self, engine, view):
        self.config = None
        self.project = None
        self.clock = None

        self.engine = engine
        self.view = view

        self.load_config()
        self.load_project()
        self.setup_clock()

        self.bind_actions()
        self.bind_shortcuts()

        #self.view.update_button.clicked.connect(self.update_data)
        #self.update_view()
    
    def load_config(self):
        self.config = RConfig()

    def load_project(self):
        self.project = RProject()
        self.project.load_project("default")

    def setup_clock(self):
        self.clock = RTimer(self.view)
        self.clock.scheduled_method = self.save
        self.clock.timeout_method = self.clear_message
        self.clock.prepare()

    def save(self):
        if self.view.is_modified():
            mainText = self.view.get_main_content()
            self.view.leave_unmodified()
            self.project.set(EnProjectFile.Flow, mainText)
            self.view.show_message("Saved")
            self.clock.setup()
    
    def clear_message(self):
        self.view.show_message("")

    def update_data(self):
        data = self.view.edit_field.text()
        self.model.set_data(data)
        self.update_view()

    def update_view(self):
        data = self.model.get_data()
        #self.view.data_display.setText(data)

    def bind_actions(self):
        print("Not implemented")

    def bind_shortcuts(self):
        self.shortcutSave = QShortcut(QKeySequence("Ctrl+S"), self.view)
        #self.shortcutInfo = QShortcut(QKeySequence("F1"), self.view)
        self.shortcutSave.activated.connect(self.save)

    