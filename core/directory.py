import os

class RDirectory:
    def __init__(self, root = ""):
        if root == "":
            root = os.getcwd()
        self.root = root
        self.projects = os.path.join(self.root, "projects") # todo: read from config. if not present - create like this
        
    def force_directory(self, path):
        if not os.path.exists(path):
            os.makedirs(path)

    def build(self):
        self.force_directory(self.projects)
        
    def get_project_path(self, project_name):
        path = os.path.join(self.projects, project_name)
        self.force_directory(path)
        return path
    
    def get_project_build_path(self, project_name):
        path = os.path.join(self.projects, project_name, "build")
        self.force_directory(path)
        return path