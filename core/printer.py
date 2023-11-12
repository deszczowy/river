import pdfkit
import subprocess
import os

class Printer:

    def __init__(self, work_directory, file):
        self.options = {
            'page-size': 'A4',
            'margin-top': '0mm',
            'margin-right': '0mm',
            'margin-bottom': '0mm',
            'margin-left': '0mm',
        }
        self.path = work_directory
        self.input_file = os.path.join(work_directory, file)
        self.output_file = "{0}.pdf".format(self.input_file) 

    def print(self):
        pdfkit.from_file(
            self.input_file, 
            self.output_file,
            options=self.options
        )

    def open(self):
        if os.name == 'posix':  # Unix/Linux
            subprocess.run(['xdg-open', self.output_file], check=True)
        elif os.name == 'nt':  # Windows
            os.startfile(self.output_file)
        else:
            raise NotImplementedError("Opening PDF is not supported on this platform.")
