def min_abs_indices(s):
    min_abs = min(map(abs, s))
    return [i for i in range(len(s)) if abs(s[i]) == min_abs]

#OR
def min_abs_indices(s):
    f = lambda i: abs(s[i]) == min_abs
    return list(filter(f, range(len(s))))

def largest_adj_sum(s):
    return max([s[i] + s[i+1] for i in range(len(s) - 1))

#OR
def largest_adj_sum(s):
    return max([a + b for a, b in zip(s[:-1], s[1:])])
    
def digit_dict(s):
    """Map each digit d to the lists of elements in s that end with d."""
    """Key is a digit and value is a list"""
    return {d: [x for x in s if x % 10 == d] for d in range(10) if any([x % 10 ==d for x in s])} #这也太长了

def digit_dict(s):
    for d in range(10):
        if any([x % 10 == d for x in s]):
            return {d: [x for x in s if x % 10 == d]}

def all_have_an_equal(s):
    """Does every element equal some other element in s?"""
    return all([s[i] in s[:i] + s[i+1:]) for i in range(len(s)])
#OR 
    return all([sum([1 for y in s if y == x]) > 1 for x in s])
#OR 
    return min([sum([1 for y in s if y == x]) for x in s]) > 1
#OR
    min([s.count(x) for x in s]) > 1

#Linked list exercises
class Link:
    empty = ()
    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __repr__(self):
        if self.rest:
            rest_repr = ', ' + repr(self.rest)
        else:
            rest_repr = ''
        return 'Link(' + repr(self.first) + rest_repr + ')'

    def __str__(self):
        string = '<'
        while self.rest is not Link.empty:
            string += str(self.first) + '> '
            self = self.rest

def ordered(s, key=lambda x: x):
    """Is Link s ordered?"""
    if s is Link.empty or s.rest is Link.empty:
        return True
    elif key(s.first) > key(s.rest.first):
        return False
    else:
        return ordered(s.rest)

def merge(s, t):
    """Return a sorted link with the elements in sorted list s and t"""
    if s is Link.empty:
        return t
    elif t is Link.empty:
        return s
    elif s.first <= t.first:
        return Link(s.first, merge(s.rest, t))
    else:
        return Link(t.first, merge(s, t.rest))

def merge_in_place(s, t):
    """Return a sorted Link with the elements of sorted s and t"""
    if s is Link.empty:
        return t
    elif t is Link.empty:
        return s
    elif s.first <= t.first:
        s.rest = merge_in_place(s.rest, t)
        return s
    else:
        t.rest = merge_in_place(s, t.rest)
        return t    
