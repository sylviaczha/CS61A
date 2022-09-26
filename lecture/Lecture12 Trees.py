# Trees

def tree(label, branches=[]):
    for branch in branches:
        assert is_tree(branch), 'branches must be trees'
    return [label] + list(branches)

def label(tree):
    return tree[0]

def branches(tree):
    '''branches always returns a list.
        if that list is not empty, every element is a tree,
        but it might be an empty list.'''
    return tree[1:]

def is_tree(tree):
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True

def is_leaf(tree):
    return not branches(tree)

### +++ === ABSTRACTION BARRIER === +++ ###

def fib_tree(n):
    """Construct a Fibonacci tree."""
    if n == 0 or n == 1:
        return tree(n)
    else:
        left = fib_tree(n - 2)
        right = fib_tree(n - 1)
        fib_n = label(left) + lable(right)
        return tree(fib_n, [left, right])

def count_leaves(tree):
    """Count the number of leaves in tree"""
    assert is_tree(tree)
    if is_leaf(tree):
        return 1
    else:
        return sum([count_leaves(b) for b in branches(tree)])

def leaves(tree):
    """Return a list containing the leaf lables of tree."""
    if is_leaf(t):
        return [label(tree)]
    else:
        return sum([leaves(b) for b in branches(tree)],[])

def print_tree(t, indent=0):
    """Print a representation of this tree in which each label is
    indented by two spaces times its depth from the root."""
    print('  ' * indent + str(label(t)))
    for b in branches(t):
        print_tree(b, indent + 1)

def increment_leaves(t):
    """Return a tree like t but with leaf labels incremented."""
    if is_leaf(t):
        return tree(label(t) + 1)
    else:
        bs = [increment_leaves(b) for b in branches(t)]
        return tree(label(t), bs)

def increment(t):
    """Return a tree like t but with all labels incremented."""
    bs = [increment(b) for b in branches(t)]
    return tree(label(t) + 1, bs]

# Some recursive functions build up their results by manipulating the return value of a recursive call.

def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)

# Other resursive functions build up their result by passing information into the recursive call as an argument.

def fact_tail(n):
    return fact_times(n, 1)

def fact_times(n, k):
    if n == 0:
        return k
    else:
        return fact_times(n - 1, k * n)

# Both of these strategies are useful when processing trees.

from tree import *
numbers = tree(3, [tree(4), tree(5, [tree(6)])])

haste = tree('h', [tree('a', [tree('s'), tree('t')]), tree('e')])

def print_sums(t, so_far):
    """Print the sum of labels along the path from the root of each leaf."""
    so_far = so_far + label(t)
    if is_leaf(t):
        print(so_far)
    else:
        for b in branches(t):
            print_sums(b, so_far)
