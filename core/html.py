class RHtml:

    def __init__(self):
        self.template = ""

    def paragraph(self, content):
        return '<p>' + content + '</p>'

    def form(self, params):
        for anchor, content in params.items():
            self.template = self.template.replace(anchor, content)

    def get(self):
        return self.template

class RMainTextHtml(RHtml):

    def __init__(self):
        super().__init__()
        self.template = """<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8"/>
    <title>%1</title>
    <style>
        body{padding: 0px; margin:0px;}
        #column{width: 50%; text-align: justify; padding: 5px; padding-right: 0px; font-size: 9pt; font-family:Georgia, 'Times New Roman', Times, serif;}
    </style>
</head>

<body>

    <div id="column">
        [%1]
    </div>
</body>
</html>"""

    def produce(self, text):
        content = ""
        lines = text.splitlines()
        for line in lines:
            content += self.paragraph(line)

        params = { '[%1]': content }
        self.form(params)