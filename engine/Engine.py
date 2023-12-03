from engine.Container import *

class REngine:
    def __init__(self):
        self.container = None
    
    def test(self, content):
        print(content)
        self.container = Container(content)
        print(self.container.get_all_notes(['congue']))
        print(self.container.get_all_notes(['congue', 'cursus']))
        print(self.container.get_all_notes(['cursus', 'congue']))