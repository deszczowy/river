from engine.Container import *
from engine.BuildHtml import *

class REngine:
    def __init__(self):
        self.container = None
    
    def test(self, content):
        self.container = Container(content)

        doc = RProjectBuild()
        doc.build(self.container)
        print(doc.get())