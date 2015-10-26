from atom import Atom, Symbol
from list import List


def test_atom():
    assert(Atom(1) == Atom(1))


def test_atom2():
    assert(Atom(1) != Atom(2))


def test_symbol():
    a1 = Symbol(1)
    a2 = Symbol(2)
    assert(a1 == a1)
    assert(a1 != a2)


def test_list():
    l1 = List([1, 2, 3])
    assert(l1.car() == 1)
    assert(l1.cdr() == List([2, 3]))


def test_list_cons():
    assert(List([1]).cons(List([2])) == List([1, 2]))


def test_list_get_item():
    assert(List()[0] is None)
    assert(List([1])[0] == 1)
