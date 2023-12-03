from engine.Functions import *

class Note:

    def __init__(self, txt, id):
        self.stoppers = {' ', '.', '\n', '?', '!', '#'}
        if id == 0:
            self.id = new_id()
        else:
            self.id = id
        self.title = ""
        self.note = ""
        self.tags = []
        self.notices = []
        self.work(txt)

    def work(self, txt):
        current = ""
        tag = ""
        notice = ""

        self.tags = []
        inTag = False
        inNotice = False

        for character in txt:
            if character != "#":
                if character == ":":
                    self.title = current
                    current = ""
                elif character == "[":
                    inNotice = True
                elif character == "]":
                    if notice != "":
                        self.notices.append(notice)
                        notice = ""
                    inNotice = False
                elif character == "@":
                    inTag = True
                    current += character
                elif character in self.stoppers:
                    current += character
                    if tag != "":
                        self.tags.append(tag)
                        tag = ""
                    inTag = False
                else:
                    if inTag:
                        tag += character
                        current += character
                    elif inNotice:
                        notice += character
                    else:
                        current += character
            else:
                break
        if tag != "":
            self.tags.append(tag)
        if notice != "":
            self.notices.append(notice)

        self.note = current
        if self.title == "":
            self.title = self.note[:20] + "..."
