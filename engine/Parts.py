class Parts:
    def __init__(self, text):
        self.parts = []
        self.read_parts(text)

    def read_parts(self, text):
        s = text.find("#")
        e = text.find("#", s +1)
        x = ""
        while s < e:
            x = text[s +1:e]
            self.parts.append(x.strip())
            s = e
            e = text.find("#", s +1)
        
        if s < len(text):
            x = text[s +1:]
            self.parts.append(x.strip())
