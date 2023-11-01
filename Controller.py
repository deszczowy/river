from core.project import RProject

class RController:
    def __init__(self, engine, view):
        self.project = RProject()
        self.engine = engine
        self.view = view

        #self.view.update_button.clicked.connect(self.update_data)
        #self.update_view()

    def update_data(self):
        data = self.view.edit_field.text()
        self.model.set_data(data)
        self.update_view()

    def update_view(self):
        data = self.model.get_data()
        #self.view.data_display.setText(data)