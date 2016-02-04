class Function():
    def __init__(self, fn=None):
        self.fn = fn

    def eval(self, env, args):
        return self.fn(env, args)
