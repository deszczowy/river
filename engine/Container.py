from engine.Dictionary import *
from engine.Parts import *
from engine.Note import *

class Container:
    def __init__(self, text):
        self.notes = []
        self.tags = Dictionary()
        self.process(text)
        self.make_tags_dictionary()

    def process(self, text):
        parts_of_script = Parts(text)
        id = 1
        for p in parts_of_script.parts:
            self.notes.append(Note(p, id))
            id += 1 
    
    def make_tags_dictionary(self):
        self.tags.clean()
        for n in self.notes:
            id = n.id
            for t in n.tags:
                self.tags.add(t, id)
        self.tags.print_me()

    def get_all_notes(self, tags):
        return list(self.tags.get_notes_for_tags(tags))
