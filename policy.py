class Policy:
    def __init__(self):
        self.V = dict()

    def __call__(self, s):
        return self.V[s] if s in self.V else 0

    def update(self, s, a):
        self.V[s] = a

    def __str__(self):
        s = ""
        for st in self.V:
           s = s + "State " + str(st)+" := Action " + str(self.V[st]) + "\n"
        return s
