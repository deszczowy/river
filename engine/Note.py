from engine.Functions import *

class Note:

    def __init__(self, txt, id):
        if id == 0:
            self.id = new_id()
        else:
            self.id = id
        self.title = ""
        self.note = ""
        self.tags = []
        self.work(txt)

    def work(self, txt):
        current = ""
        tag = ""
        self.tags = []
        inTag = False

        for character in txt:
            if character != "#":
                if character == ":":
                    self.title = current
                    current = ""
                elif character == "@":
                    inTag = True
                    current += character
                elif character == " " or character == "\n":
                    current += character
                    if tag != "":
                        self.tags.append(tag)
                        tag = ""
                    inTag = False
                else:
                    if inTag:
                        tag += character
                    current += character
            else:
                break
        if tag != "":
            self.tags.append(tag)
        self.note = current
        if self.title == "":
            self.title = self.note[:20] + "..."
        
        print("Id: ", self.id)
        print("Title: ", self.title)
        print("Content: ", self.note)
        print("Tags: ", self.tags)
