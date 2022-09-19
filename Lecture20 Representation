class Bear:
    """A Bear."""

    def __init__(self):
        self.__repr__ = lambda: 'oski'
        self.__str__ = lambda: 'this bear'

    def __repr__(self):
        return 'Bear()'

    def __str__(self):
        return 'A bear'


oski = Bear()
print(oski)
print(str(oski))  # class attribute
print(repr(oski))  # class attribute
print(oski.__str__())  # instance attribute
print(oski.__repr__())  # instance attribute

# print(oski) and print(str(oski)) are always the same.
# print(str(oski)) is a class attribute.
# print(repr(oski)) is a class attribute and also a function.
# print(oski.__str__()) and print(oski.__repr__) look up in the conventional way.


def repr(x):
    """replace the built in repr function."""
    return type(x).__repr__(x)


def str(x):
    t = type(x)
    if hasattr(t, '__str__'):
        return t.__str__(x)
    else:
        return repr(x)


class Ratio:
    # type dispatching and type coercion
    def __init__(self, n, d):
        self.numer = n
        self.demom = d

    def __repr__(self):
        return 'Ratio({0}, {1})'.format(self.numer, self.denom)

    def __str__(self):
        return '{0}/{1}'.format(self.numer, self.denom)

    def __add__(self, other):
        if isinstance(other, int):
            n = self.numer + self.denom * other
            d = self.denom
        elif isinstance(other, Ratio):
            n = self.numer * other.denom + self.denom * other.numer
            d = self.denom * other.denom
        elif isinstance(other, float):
            return float(self) + other
        g = gcd(n, d)
        return Ratio(n//g, d//g)
    __radd__ = __add__

    def __float__(self):
        return self.numer/self.denom


def gcd(n, d):
    while n != d:
        n, d = min(n, d), abs(n-d)
    return n


class Kangaroo:
    """Write a class named Kangaroo with:
    constructor initialises an instance variable named "pouch_contents" to an empty list.

    pouch_contents takes a string as input and adds it to pouch contents,
    if it is not already in the pouch. If it is already in the pouch, print
    "object already in pouch".

    __str__ prints content of pouch.
    If the pouch is empty,then print "The kangaroo's pouch is empty."
    If the pouch is not empty, then print "The kangaroo's pouch contains:
    [A,B,C]" (where A, B, C are the contents of the pouch).

    Write a short driver that tests your class.
    """

    def __init__(self):
        self.pouch_contents = []

    def put_in_pouch(self, x):
        for i in range(len(self.pouch_contents)):
            if (self.pouch_contents[i] == x):
                print("already in the pouch")
                return
        self.pouch_contents.append(x)

    def __str__(self):
        if(len(self.pouch_contents) == 0):
            return "The Kangaroo's pouch is empty."
        else:
            return "The Kangaroo's pouch contains: " + \
                   str(self.pouch_contents)
