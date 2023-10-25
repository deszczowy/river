import os

class Directory:
    def __init__(self):
        self.root = os.getcwd()
        self.projects = full_path = os.path.join(self.root, "projects") # todo: read from config. if not present - create like this
        
    def force_directory(self, path):
        if not os.path.exists(path):
            os.makedirs(path)

    def build(self):
        self.force_directory(self.projects)
        
    def get_project_path(self, projectName):
        path = os.path.join(self.projects, projectName)
        self.force_directory(path)
        return path