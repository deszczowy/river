import os
from Core import RMainTextHtml, RPrinter

class RBuild:
    def __init__(self, root):
        self.root = ""
        self.printout = "print.html"
        self.setup(root)

    def setup(self, directory):
        self.root = directory

    def store(self, file_path, file_content):
        try:
            with open(file_path, 'w') as file:
                file.write(file_content)
        except Exception as e:
            print(f"An error occurred: {e}")
    
    def print_main_text(self, content):
        mth = RMainTextHtml()
        mth.produce(content)

        f = os.path.join(self.root, self.printout)
        c = mth.get()

        self.store(f, c)

        p = RPrinter(f)
        p.print()
        p.open()

