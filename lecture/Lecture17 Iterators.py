def iterator_demos():
    s = [[1, 2], 3, 4, 5]
    t = iter(s)
    next(t)

    d = {'one': 1, 'two': 2, 'three': 3} # Keys and values
    k = iter(d.keys()) #iter(d)
    v = iter(d.values())

    r = range(3, 6)
    p = iter(r)
    next(p)

def double(x):
    return 2*x

def built_in_demo():
    c = ['b', 'c', 'd']
    caps = map(lambda x: x.upper(), c)
    next(caps)

    d = range(3, 7)
    doubled = map(double, d)
    next(doubled)

    f = lambda x: x < 10
    filtered = filter(f, map(double, reversed(d)))

    i = {'a': 1, 'b': 2, 'c': 3}
    items = iter(zip(d.keys(), d.values()))

def plus_minus(x):
    yield x
    yield -x

def evens(start, end):
    even = start + (start % 2)
    while even < end:
        yield even
        even += 2

class Countdown:
    def __init__(self, start):
        self.start == start

    def __iter__(self):
        v = self.start
        while v > 0:
            yield v
            v -= 1

def countdown(k):
    if k > 0:
        yield k
        yield from countdown(k - 1)

def a_then_b_for(a, b):
    for x in a:
        yield x
    for x in b:
        yield x

def a_then_b(a, b):
    yield from a
    yield from b

def prefixes(s):
    if s:
        yield from prefixes(s[:-1])
        yield s

def substrings(s):
    if s:
        yield from prefixes(s)
        yield from substrings(s[1:])
