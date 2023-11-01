import os

from directory import Directory
from file import File
from enum import Enum

empty_header = """title=
author=
overview="""

class ProjectFile(Enum):
    Header = 0
    Flow = 1
    Note = 2

class Project:
    def __init__(self):
        self.directory = Directory()
        self.file = File()
        self.path = ""
        self.fileNames = {
            ProjectFile.Header: "header.rvr",
            ProjectFile.Flow: "main.rvr",
            ProjectFile.Note: "notes.rvr"
        }
        
    def load_project(self, name):
        self.path = self.directory.get_project_path(name)
        self.file.set_root(self.path)
        self.check_structure()
        
    def check_structure(self):
        for item in ProjectFile:
            self.check_if_file_present(item)
        
    def get_file_name(self, kind):
        return self.fileNames.get(kind, "")
        
    def check_if_file_present(self, kind):
        file = self.get_file_name(kind)
        if file == "":
            return False
        
        path = os.path.join(self.path, file)

        if not os.path.exists(path) or not os.path.isfile(path):
            self.create_file(kind)
        return True

    def create_file(self, kind):
        if kind == ProjectFile.Header:
            self.create_header()
        else:
            self.create_empty_file(kind)

    def create_header(self):
        name = self.get_file_name(ProjectFile.Header)
        self.file.create(name, empty_header)

    def create_empty_file(self, kind):
        name = self.get_file_name(kind)
        self.file.create(name)
        
    def get(self, kind):
        file = self.get_file_name(kind)
        return self.file.get_content(file)

    def set(self, kind, content):
        file = self.get_file_name(kind)
        return self.file.save_content(file, content)

p = Project()
p.load_project("test4")
print(p.get(ProjectFile.Header))
p.set(ProjectFile.Note, "Test")
print(p.get(ProjectFile.Note))