from engine.Container import *
from engine.BuildHtml import *

class REngine:
    def __init__(self):
        self.container = None
    
    def build(self, content, path):
        self.container = Container(content)
        self.container = None

    
    def test(self, content):
        self.container = Container(content)