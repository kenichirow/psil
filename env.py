class Environment(dict):
    def __init__(self, parent=None):
        self.parent = parent

    def push(self, label, sexpr):
        if label.data in self:
            raise Exception('{} are already exists'.format(label))
        self[label.data] = sexpr.data

    def find(self, key):
        label = key.data
        if label in self:
            return self[label]
        else:
            return self.parent.find(label)
