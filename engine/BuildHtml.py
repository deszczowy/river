from Core import RHtml
from engine.Container import Container
from engine.Dictionary import Dictionary
from engine.Note import Note

class RProjectBuild(RHtml):

    def __init__(self):
        super().__init__()
        self.card_template = "<div>{}{}</div>"
        self.template = "<!DOCTYPE html>[%1]"
    
    def build(self, container):
        cards = ""
        for note in container.notes:
            cards += self.card(note)
        
        params = {'[%1]': cards}
        self.form(params)        

    def card(self, note):
        title = self.paragraph(note.title)
        text = self.paragraph(note.note)
        return self.card_template.format(title, text)
        