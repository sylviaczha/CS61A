# Countainers

digits = [1, 8, 2, 8]

# the number of elements
len(digits)

# an element selected by its index
digits[3] or getitem(digits, 3)

# concatenation and repetition
[2, 7] + digits * 2 or add([2, 7], mul(digits, 2))

# nested lists
pairs = [[10, 20], [30, 40]]
pairs[1]
pairs[1][0]

# For statements

def count_while(s, value)：
    """count the number of times that value occurs in the sequence s"""
    total, index = 0, 0
    while index < len(s):
        if s[index] == value:
            total += 1
        index += 1
    return total

def count_for(s, value):
    """Count the number of times that value occurs in the sequence s"""
    total = 0
    for element in s:
        if element == value:
            total += 1
    return total

def count_same(pairs):
    """Return how many pairs have the same element repeated.
    >>> pairs = [[1, 2], [2, 2], [2, 3], [4, 4]]
    >>> count_same(pairs)
    2
    """
    same_count = 0
    for x, y in pairs:
        if x == y:
            same_count += 1
    return same_count

# Ranges

list(range(5, 8))
list(range(4))
len(range(4))

def sum_below(n):
    total = 0
    for i in range(n):
        total += i
    return total += i

def sum_iter(L):
    """Iteratively sum first n integers."""
    total = 0
    for i in range(L):
        total += i
    return total

def sum_iter2(n):
    total = 0
    for i in range(0, n+1):
        total += i
    return total 

def sum_rec(L):
    """Recursively sum first n integers."""
    if L == []:
        return 0
    else:
        return L[0] + sum_rec(L[1:])

def sum_rec2(n):
    if n == 0:
        return 0
    else:
        return n + sum_rec2(n-1)

def cheer():
    for _ in range(3):
        print('Go Bears!')


# List comprehension

odds = [1, 3, 5, ,7, 9]
[x + 1 for x in odds]
[x for x in odds if 25 % x == 0]

def divisors(n):
    """Return the integers that evenly divide n."""
    return [1] + [x for x in range(2, n) if n % x == 0]

def divisors1(n):
    for x in range(2, n):
        if n % x == 0:
            return [1] + [x]

# String reversal
def reverse_string(s):
    """Reverse a string s."""
    if len(s) == 1:
        return s
    else:
        return reverse(s[1:]) + s[0]
