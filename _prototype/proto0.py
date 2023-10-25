import uuid

def new_id():
    return str(uuid.uuid4().hex)

def read_file(file_name):
    if file_name == None:
        file_name = "./doc.txt"

    content = ""
    with open (file_name, mode="r", encoding="utf-8") as cfile:
        lines = cfile.readlines()

    for line in lines:
        content += line.strip() + "\n"

    return content

class Dictionary:
    def __init__(self):
        self.dictionary = dict([])

    def add(self, key, value):
        if key not in self.dictionary:
            self.dictionary[key] = []
        self.dictionary[key].append(value)

    def print_me(self):
        print(self.dictionary)

    def get(self, key):
        return self.dictionary.get(key, None)

    def clean(self):
        self.dictionary.clear()

    def get_notes_for_tags(self, tags):
        result = set()
        for tag in tags:
            notes = self.get(tag)
            for note in notes:
                result.add(note)
        return result
        
class Storage:
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

"""
txt = read_file(None)
s = Storage(txt)
print(s.get_all_notes(['congue']))
print(s.get_all_notes(['congue', 'cursus']))
print(s.get_all_notes(['cursus', 'congue']))
"""