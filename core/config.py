from pathlib import Path

class RConfig:

    def __init__(self):
        self.settings = dict([])
        self.setup_defaults()
        path = "./app.config"

        if Path(path).is_file():
            content = self.get_file_contents(path)
            for line in content:
                self.read(line)

    def setup_defaults(self):
        self.settings.clear()
        self.settings['project_root'] = "./"

    def read(self, line):
        i = line.find("=")
        if i > 0:
            key = line[:i]
            value = line[i+1:]
            self.settings[key] = value

    def get_file_contents(self, path):
        content = []
        with open(path, mode="r", encoding="utf-8") as _file:
            content = _file.readlines()
        return content
