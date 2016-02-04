class Atom():

    def __init__(self, data):
        self.data = data

    def __eq__(self, rhs):
        if isinstance(rhs, Atom):
            return self.data == rhs.data
        else:
            return False

    def eval(self, env, args=None):
        return self.data


class Symbol(Atom):

    def __init__(self, data):
        Atom.__init__(self, data)

    def __repr__(self):
        return "Symbol:{} type: {} ".format(self.data, type(self.data))

    def __hash__(self):
        return hash(self.data)

    def __eq__(self, rhs):
        return self.data == rhs.data

    def eval(self, env, args=None):
        return env.get(self.data)


class Number(Symbol):
    def __init__(self, data):
        Atom.__init__(self, data)

    def eval(self, env, args=None):
        return self.data


TRUE = Symbol('t')
