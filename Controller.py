from Core import RProject, RConfig, RTimer

class RController:
    def __init__(self, engine, view):
        self.config = None
        self.project = None
        self.clock = None

        self.engine = engine
        self.view = view

        self.load_config()
        self.load_project()

        #self.view.update_button.clicked.connect(self.update_data)
        #self.update_view()
    
    def load_config(self):
        self.config = RConfig()

    def load_project(self):
        self.project = RProject()

    def setup_clock(self):
        self.clock = RTimer()
        self.clock.scheduled_method = self.save
        self.clock.timeout_method = self.clear_message

    def save(self):
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

    