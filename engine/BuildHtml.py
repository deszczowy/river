from Core import RHtml
from engine.Container import Container
from engine.Dictionary import Dictionary
from engine.Note import Note

class RProjectBuildHtml(RHtml):

    def __init__(self):
        super().__init__()
        self.build_templates()
    
    def build_templates(self):
        self.style_sheet = """body {padding: 0; margin: 0; background-color: black; width: 300px; margin: 0 auto;}
.card { 
	border: 1px solid #444; 
	border-radius: 5px; 
	min-height: 50px; 
	min-width: 100px;
	color: #444;
	font-family: courier;
	padding: 3px;
	background-color: #bbb;
}
.caption {padding: 0; margin:0;}
.number {font-size: 26px; padding: 3px; font-weight: bold;}
.content {}
.tag {text-decoration: none; font-size: 11px; border: 1px solid black; border-radius: 3px; margin: 1px;}
.red {border-color: red; background-color: red; color: white; }
.yellow {border-color: yellow; background-color: yellow; color: black; }
.arrow {border:0; color: #bbb; font-size: 25px; text-align: center;}
"""
        self.arrow = """<div class="arrow">&#8659;</div>"""

        self.tag_template = """<a class="tag [%p_color]" href="[%p_id]">@[%p_name]</a>"""
        
        self.card_template = """<div class="card">
	<p class="caption"><span class="number">#[%p_id]&nbsp;</span> [%p_title]</p>
	<p class="content">[%p_content]</p>
	[%p_tags]
</div>[%p_arrow]"""

        self.template = """<!DOCTYPE html>
<html>
<head>
<title>Build</title>
</head>
<style>
[%1]
</style>
<body>
[%2]
</body>
</html>
"""
    
    def build(self, container):
        cards = ""
        for note in container.notes:
            cards += self.card(note)
        
        params = {
            '[%1]': self.style_sheet,
            '[%2]': cards
        }

        self.form(params)

    def card(self, note):
        tags = ""
        for t in note.tags:
            tags += self.tag(t)

        params = {
            '[%p_id]': str(note.id),
            '[%p_title]': self.paragraph(note.title),
            '[%p_content]': self.paragraph(note.note),
            '[%p_tags]': tags,
            '[%p_arrow]': self.arrow
        }

        return self.fill_template(self.card_template, params)
    
    def tag(self, tag_data):
        params = {
            '[%p_id]': "",
            '[%p_color]': "red",
            '[%p_name]': tag_data
        }

        return self.fill_template(self.tag_template, params)