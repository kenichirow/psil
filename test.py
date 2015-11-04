from atom import Atom, Symbol
from list import List
from main import Reader
# from env import Environment


def test_atom():
    assert(Atom(1) == Atom(1))


def test_atom2():
    assert(Atom(1) != Atom(2))


def test_symbol():
    a1 = Symbol(1)
    a2 = Symbol(2)
    assert(a1 == a1)
    assert(a1 != a2)


def test_symbol_eq():
    return Symbol(1) == Symbol(1)


def test_list():
    l1 = List([1, 2, 3])
    assert(l1.car() == 1)
    assert(l1.cdr() == List([2, 3]))
    assert(List().cdr() == List())


def test_list_cons():
    assert(List([1]).cons(List([2])) == List([1, 2]))


def test_list_get_item():
    assert(List()[0] is None)
    assert(List([1])[0] == 1)


def test_expr():
    r = Reader("(1 2)")
    s = r.get_sexpr()
    assert(s == List(["1", "2"]))

    r = Reader("('foobar' 2)")
    s = r.get_sexpr()
    assert(s == List(["'foobar'", "2"]))


def test_multiline():
    with open('./multiline', 'r') as f:
        lines = ' '.join(f.readlines())
        r = Reader(lines)
        expr = r.get_sexpr()
        assert(type(expr.cdr()[1] == Symbol('2')))


def test_nest_expr():
    r = Reader("(1 (1 2))")
    s = r.get_sexpr()
    assert(s.car() == "1")
    assert(s.cdr().car() == List(["1", "2"]))
# def test_env():
#     env = Environment()
#     cdr = List([Symbol("1"), Symbol("2")])
#     env.set(List(["foo", cdr]))
#     foo = env.get("foo")
#     assert(foo is not None)
#     assert(foo.car() == Symbol("1"))
