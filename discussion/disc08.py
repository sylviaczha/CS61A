from operator import mul

class Link:
    empty = ()
    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __repr__(self):
        if self.rest:
            rest_str = ', ' + repr(self.rest)
        else:
            rest_str = ''
        return 'Link({0}{1})'.format(repr(self.first), rest_str)

    def __str__(self):
        string = '<'
        while self.rest is not Link.empty:
            string += str(self.first) + ' '
            self = self.rest
        return string + str(self.first) + '>'


"""2.1"""
def sum_nums(lnk):
    if lnk.rest is Link.empty:
        return lnk.first
    else:
        return lnk.first + sum_nums(lnk.rest)

a = Link(1, Link(6, Link(7)))
print(sum_nums(a))


"""2.2"""
def multiply_lnks(lst_of_lnks):
    val = 1
    lst = []
    for links in lst_of_lnks:
        if links is Link.empty:
            return Link.empty
        else:
            val *= links.first
            lst.append(links.rest)
    return Link(val, multiply_lnks(lst))

a = Link(2, Link(3, Link(5)))
b = Link(6, Link(4, Link(2)))
c = Link(4, Link(1, Link(0, Link(2))))
p = multiply_lnks([a, b, c])
print(repr(p))


"""2.3"""
def flip_two(lnk):
    if lnk == Link.empty or lnk.rest == Link.empty:
        return
    else:
        lnk.first, lnk.rest.first = lnk.rest.first, lnk.first
        return flip_two(lnk.rest.rest)
    
one_link = Link(1)
flip_two(one_link)
print(repr(one_link))
lnk = Link(1, Link(2, Link(3, Link(4, Link(5)))))
flip_two(lnk)
print(repr(lnk))


"""2.4"""
def filter_link(link, f):
    if link is Link.empty:
        return
    else:
        if f(link.first):
            yield link.first
        yield from filter_link(link.rest, f)


def filter_link_iter(link, f):
    while link != Link.empty:
        if f(link.first):
            yield link.first
        link = link.rest

      
link = Link(1, Link(2, Link(3)))
g = filter_link(link, lambda x: x % 2 == 0)
print(list(g))
print(list(filter_link(link, lambda x: x % 2 != 0)))



class Tree:
    def __init__(self, label, branches=[]):
        for b in branches:
            assert isinstance(b, Tree)
        self.label = label
        self.branches = branches
        
    def is_leaf(self):
        return not self.branches

"""3.1"""
def make_even(t):
    if t.label % 2 == 0:
        t.label = t.label
    else:
        t.label = t.label + 1  
    
    if t.is_leaf():
        return
    else:
        for b in t.branches:
            make_even(b)


def make_even2(t):
    if t.label % 2 == 0:
        t.label = t.label
    else:
        t.label = t.label + 1

    if t.is_leaf():
        return Tree(t.label)
    else:
        return Tree(t.label, [make_even2(b) for b in t.branches])
    

t = Tree(1, [Tree(2, [Tree(3)]), Tree(4), Tree(5)])
make_even2(t)
print(t.label)
print(t.branches[0].branches[0].label)


"""3.2"""
def square_tree(t):
    t.label = t.label ** 2
    
    if t.is_leaf():
        return
    else:
        for b in t.branches:
            square_tree(b)


def square_tree2(t):
    t.label = t.label ** 2
    
    if t.is_leaf():
        return Tree(t.label)
    else:
        return Tree(t.label, [square_tree2(b) for b in t.branches])
        
t = Tree(1, [Tree(2, [Tree(3)]), Tree(4), Tree(5)])
squared = square_tree2(t)
print(t.label)
print(t.branches[2].label)


"""3.3"""
def find_paths(t, entry):
    paths = []
    if t.label == entry:
        return [[t.label]]
    else:
        for b in t.branches:
            for lst in find_paths(b, entry):
                paths.append([t.label] + lst)
    return paths


def find_paths_rec(t, entry):
    if t.label == entry:
        return [t.label]
    else:
        return [[t.label] + find_paths_rec(b, entry) for b in t.branches]


tree_ex = Tree(2, [Tree(7, [Tree(3), Tree(6, [Tree(5), Tree(11)])]), Tree(1, [Tree(5)])])
print(find_paths(tree_ex, 5))


"""3.4"""
def combine_tree(t1, t2, combiner):
    if t1.is_leaf():
        return Tree(combiner(t1.label, t2.label))
    else:
        for b in zip(t1.branches, t2.branches):
            return Tree(combiner(t1.label, t2.label), [combine_tree(b[0], b[1], combiner)])

a = Tree(1, [Tree(2, [Tree(3)])])
b = Tree(4, [Tree(5, [Tree(6)])])
combined = combine_tree(a, b, mul)
print(combined.label)
print(combined.branches[0].branches[0].label)


"""3.5"""
def alt_tree_map(t, map_fn):
    def helper(t, map_fn, level=0):
        if level % 2 == 0:
            t.label = map_fn(t.label)
        else:
            t.label = t.label
        
        if t.is_leaf():
            return Tree(t.label)
        else:
            return Tree(t.label, [helper(b, map_fn, level + 1) for b in t.branches])

    return helper(t, map_fn)

t = Tree(1, [Tree(2, [Tree(3)]), Tree(4)])
altered = alt_tree_map(t, lambda x: -x)
print(altered.label)
print(altered.branches[0].branches[0].label)
print(altered.branches[1].label)
