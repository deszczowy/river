from engine.Functions import *
from enum import Enum

class EnProcessMode(Enum):
    Normal = 0
    Tag = 1
    Notice = 2

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

        self.proceed(txt)

    def setup(self):
        # temps
        self.current = ""
        self.tag = ""
        self.notice = ""
        self.mode = EnProcessMode.Normal

    def proceed(self, text):
        self.setup()

        for c in text:
            if c == "#":
                continue
            
            if c in self.stoppers:
                self.pause(c)
            elif c == "@":
                self.start_tag()
            elif c == ":":
                self.retrieve_title()
            elif c == "[":
                self.start_notice()
            elif c == "]":
                self.close_notice()
            else:
                self.store_char(c)

        self.close_note()
        #self.print_me()
    
    def pause(self, char):
        if self.mode == EnProcessMode.Notice:
            self.notice += char
        else:
            if self.mode == EnProcessMode.Tag:
                self.close_tag()
            self.current += char

    def close_tag(self):
        if self.tag != "":
            self.tags.append(self.tag)
            self.tag = ""
        self.mode = EnProcessMode.Normal

    def start_tag(self):
        if self.mode == EnProcessMode.Notice:
            self.notice += "@"
        else:
            if self.mode == EnProcessMode.Tag:
                self.close_tag()
            self.mode = EnProcessMode.Tag
            self.current += "@"

    def retrieve_title(self):
        self.title = self.current
        self.current = ""
    
    def start_notice(self):
        self.mode = EnProcessMode.Notice
    
    def close_notice(self):
        self.mode = EnProcessMode.Normal
        if self.notice != "":
            self.notices.append(self.notice)
        self.notice = ""

    def close_note(self):
        self.close_tag()
        self.close_notice()
        
        self.note = self.current
        if self.title == "":
            self.title = self.note[:20] + "..."
    
    def store_char(self, char):
        if self.mode == EnProcessMode.Notice:
            self.notice += char
        else:
            if self.mode == EnProcessMode.Tag:
                self.tag += char
            self.current += char
    
    def print_me(self):
        print(":: {}".format(self.id))
        print("Title: {}".format(self.title))
        print("Content: {}".format(self.note))
        print("Tags: ")
        for t in self.tags:
            print("   {}".format(t))
        print("Notices: ")
        for n in self.notices:
            print(" * {}".format(n))