def tree(label, branches=[]):
    """Construct a tree with the given lable calue and a list of branches."""
    return [label] + list(branches)

def label(tree):
    """Return the lable value of a tree."""
    return tree[0]

def branches(tree):
    """Return the list of branches of a tree."""
    return tree[1:]

def is_leaf(tree):
    """Returns True if the list of branches is empty, and False otherwise."""
    return not branches(tree)

def print_tree(t, indent=0):
    """Print a representation of this tree in which each node is
    indented by two spaces times its depth from the root."""
    print('  ' * indent + str(label(t)))
    for b in branches(t):
        print_tree(b, indent + 1)

def height(t):
    """Return the height of a tree."""
    if is_leaf(t):
        return 0
    else:
        return 1 + max([height(b) for b in branches(t)])

def max_path_sum(t):
    """Return the maximum path sum of the tree."""
    if is_leaf(t):
        return label(t)
    else:
        return label(t) + max([max_path_sum(b) for b in branches(t)])

def square_tree(t):
    """Return a tree with the square of every element in t."""
    if is_leaf(t):
        return tree(label(t)**2, [])
    else:
        return tree(label(t)**2, [square_tree(b) for b in branches(t)])

def find_path(t, x):
    if label(t) == x:
        return [label(t)]
    for b in branches(t):
        path = find_path(b, x)
        if path:
            return [label(t)] + path

def prune_binary(t, nums):
    if is_leaf(t):
        if label(t) in nums:
            return t
        return None
    else:
        next_valid_nums = [num[1:] for num in nums if num[0] == label(t)]
        new_branches = []
        for b in branches(t):
            pruned_branch = prune_binary(b, next_valid_nums)
            if pruned_branch is not None:
                new_branches = new_branches + [pruned_branch]
        if not new_branches:
            return None
        return tree(label(t), new_branches)

t = tree('1',[tree('0',[tree('0'), tree('1')]),tree('1',[tree('0')])])
new_t = print_tree(prune_binary(t, ['01', '110', '100']))
print(new_t)
