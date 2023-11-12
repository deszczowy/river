import os

from core.directory import RDirectory
from core.file import RFile
from enum import Enum

class EnProjectFile(Enum):
    Header = 0
    Flow = 1
    Note = 2

class RProject:
    def __init__(self, working_directory):
        self.initialize(working_directory)
    
    def initialize(self, root):
        self.name = ""
        self.file = RFile()
        self.directory = RDirectory(root)
        self.path = self.directory.projects

        self.fileNames = {
            EnProjectFile.Header: "header.rvr",
            EnProjectFile.Flow: "main.rvr",
            EnProjectFile.Note: "notes.rvr"
        }

    def get_root(self):
        return self.directory.projects

    def get_build_directory(self):
        return self.directory.get_project_build_path(self.name)
    
    def get_current_name(self):
        return self.name
        
    def load_project(self, name):
        self.path = self.directory.get_project_path(name)
        self.name = name
        self.file.set_root(self.path)
        self.check_structure()
        
    def check_structure(self):
        for item in EnProjectFile:
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
        if kind == EnProjectFile.Header:
            self.create_header()
        else:
            self.create_empty_file(kind)

    def create_header(self):
        name = self.get_file_name(EnProjectFile.Header)
        content = self.create_header_content("", "", "")
        self.file.create(name, content)

    def create_empty_file(self, kind):
        name = self.get_file_name(kind)
        self.file.create(name)
        
    # working with files content
    def get(self, kind):
        file = self.get_file_name(kind)
        return self.file.get_content(file)

    def set(self, kind, content):
        file = self.get_file_name(kind)
        return self.file.save_content(file, content)

    def create_header_content(self, title, author, overview):
        content = ""
        content += "title={0}\n".format(title)
        content += "author={0}\n".format(author)
        content += "overview={0}\n".format(overview)
        return content

    def update_header_file(self, title, author, overview):
        content = self.create_header_content(title, author, overview)
        self.set(EnProjectFile.Header, content)