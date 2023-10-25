import os

class File:
    def __init__(self):
        self.root = ""
    
    def set_root(self, path):
        self.root = path

    def create(self, name, content = ""):
        file_path = os.path.join(self.root, name)

        with open(file_path, 'w') as file:
            file.write(content)
    
    def get_content(self, name):
        file_path = os.path.join(self.root, name)
        file_contents = ""
        try:
            with open(file_path, 'r') as file:
                file_contents = file.read()
        except FileNotFoundError:
            print(f"File '{file_path}' not found.")
        except Exception as e:
            print(f"An error occurred: {e}")
        return file_contents

    def save_content(self, name, content):
        file_path = os.path.join(self.root, name)
        try:
            with open(file_path, 'w') as file:
                file.write(content)
        except Exception as e:
            print(f"An error occurred: {e}")