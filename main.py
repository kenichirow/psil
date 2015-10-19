from optparse import OptionParser

__version__ = '0.0.1'


def _plus(lhs, rhs):
    return int(lhs) + int(rhs)


FUNCTIONS = {'+': _plus}
SPECIAL_FORMS = '()'


class Reader:
    def __init__(self, string=None):
        self.source = string
        self.index = 0
        self.expressions = []
        print self.process(self.source)
        self.level = 1

    def execute(self, commands):
        if commands != []:
            commands.reverse()
            s = commands.pop()
            if s in FUNCTIONS.keys():
                return FUNCTIONS[s](*commands)

    def create_command(self, source):
        tokens = []
        for i, n in enumerate(source):
            self.index += 1
            if n == '(':
                tokens.append(self.create_command(source[self.index:]))
            if n == ')':
                break
            if n not in SPECIAL_FORMS and n != ' ':
                tokens.append(n)
        return tokens

    def process(self, source):
        if len(source) == 0:
            return
        commands = []
        while self.index < len(source):
            token = source[self.index]
            if token == ' ':
                continue
            if token == '(':
                self.index += 1
                commands = self.create_command(source[self.index:])
                print commands
        return self.execute(commands)


if __name__ == '__main__':
    p = OptionParser(version="ver:%s" % __version__)
    p.add_option('-f', '--file', help='target file')
    opts, args = p.parse_args()
    if opts.file:
        with open(opts.file, 'r') as f:
            lines = f.readlines()
            for line in lines:
                r = Reader(line.strip())
    else:
        print 'need file name'
