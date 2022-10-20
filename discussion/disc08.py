




def find_paths(t, entry):
   paths = []
   if t.label == entry:
       return [t.label]
   for b in t.branches:
       if find_paths(b, entry):
           paths.append([t.label] + find_paths(b, entry))
   return paths

class Tree:
    def __init__(self, label, branches=[]):
        for b in branches:
            assert isinstance(b, Tree)
        self.label = label
        self.branches = branches

    def is_leaf(self):
        return not self.branches

tree_ex = Tree(2, [Tree(7, [Tree(3), Tree(6, [Tree(5), Tree(11)])]), Tree(1, [Tree(5)])])
print(find_paths(tree_ex, 5))
