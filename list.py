class Quote():
    def __init__(self):
        pass

    def eval(self):
        return self.cdr()


class List():
    def __init__(self, data=None):
        self.data = data or []

    def car(self):
        return self.data[0]

    def cdr(self):
        return List(self.data[1:])

    def __eq__(self, rhs):
        return self.data == rhs.data

    def __iter__(self):
        return self.data.__iter__()

    def __getitem__(self, index):
        try:
            return self.data[index]
        except IndexError:
            return None

    def cons(self, rhs):
        return List(self.data + rhs.data)

    def eval(self, env):
        # 環境にbindされたdataを取得する
        # functionだった場合は
        form = self.car().eval(env)
        return form.eval(env, self.cdr())
