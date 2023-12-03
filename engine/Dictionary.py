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
            if notes != None:
                for note in notes:
                    result.add(note)
        return result