class One:
    def p(self):
        print("p")

class Two:
    method = None

    def go(self):
        if self.method != None:
            self.method()

class Three:
    def __init__(self):
        one = One()
        two = Two()

        two.method = one.p
        two.go()

t = Three()