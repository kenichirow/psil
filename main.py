import string
from atom import Symbol
from optparse import OptionParser
from env import Environment
from function import Function

from list import List


__version__ = '0.0.1'

SPECIAL_FORMS = '()'
DELIM = string.whitespace + SPECIAL_FORMS


class Reader:
    def __init__(self, string=None):
        self.source = string
        self.index = 0
        self.length = len(string)
        self.expressions = []
        self.level = 1

    def get_sexpr(self):
        expr = []
        token = self.get_token()
        # start of sexpr
        if token == "(":
            token = self.get_token()
            expr.append(token)
            while token != ')':
                self.next()
                token = self.get_token()

                if token is None:
                    break

                elif token == "(":
                    self.prev()
                    child = self.get_sexpr()
                    expr.append(child)
                elif token == ")":
                    self.prev()
                else:
                    expr.append(token)

        return List(expr)

    def get_token(self):
        token_str = ""
        if self.index == self.length:
            return None
        if self.current() in SPECIAL_FORMS:
            self.next()
            return self.previous()

        while self.index < self.length - 1:
            if self.current() in DELIM:
                break
            else:
                token_str = token_str + self.current()
                self.next()
        return token_str

    def next(self):
        self.index += 1

    def prev(self):
        self.index -= 1

    def current(self):
        return self.source[self.index]

    def previous(self):
        return self.source[self.index-1]


def setup_global_env(self, env):
    env.push(Symbol("define"), Function(self.define))
    env.push(Symbol("eq"), Function(self.eq))
    env.push(Symbol("car"), Function(self.car))
    env.push(Symbol("cdr"), Function(self.cdr))


if __name__ == '__main__':
    p = OptionParser(version="ver:%s" % __version__)
    p.add_option('-f', '--file', help='target file')
    opts, args = p.parse_args()
    env = Environment()

    setup_global_env(env)

    if opts.file:
        with open(opts.file, 'r') as f:
            lines = f.readlines()
            for line in lines:
                r = Reader(line.strip())
                r.get_sexpr()
    else:
        print 'need file name'
