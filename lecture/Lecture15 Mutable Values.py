# The primary mechanism by which objects have behaviour is through their attributes.
# We access the attribute of an object through a dot expression.

# Declare the name 'balance' nonlocal at the top of the body of the function in which it is re-assigned.

def make_withdraw(balance):
    """Return a withdraw function with a starting balance."""
    def withdraw(amount):
        nonlocal balance
        if amount > balance:
            return 'Insufficient funds'
        balance = balance - amount
        return balance
    return withdraw


def make_withdraw_list(balance):
    b = [balance]
    def withdraw(amount):
        if amount > b[0]:
            return 'Insufficient funds'
        b[0] = b[0] - amount
        return b[0]
    return withdraw

def date_demos():
    from datetime import date
    today = date(2020, 2, 24)
    freedom = date(2020, 5, 20)
    str(freedom - today)
    today.year
    today.strftime('%A, %B %d')
    type(today)

def string_demos():
    "Hello".lower()
    "Hello".upper()
    "Hello".swapcase()
    hex(ord('A'))
    print('\a')
    print('1\n2\n3')
    from unicodedata import lookup, name
    name('A')
    lookup('SNOWMAN')
    lookup('SOCCER BALL')
    lookup('BABY')
    s = lookup('SNOWMAN')

def list_demos():
    suits = ['coin', 'string', 'myriad']  # A list literal
    original_suits = suits
    suits.pop()               # Removes and returns the final element
    suits.remove('string')    # Removes the first element that equals the argument
    suits.append('cup')       # Add an element to the end
    suits.extend(['sword', 'club'])  # Add all elements of a list to the end
    suits[2] = 'spade'               # Replace an element
    suits[0:2] = ['heart', 'diamond']  # Replace a slice
    [suit.upper() for suit in suits]
    [suit[1:4] for suit in suits if len(suit) == 5]

def dict_demos():
    numerals = {'I': 1, 'V': 5, 'X': 10}
    numerals['X']
    numerals['I'] = 1
    numerals['L'] = 50
    numerals
    sum(numerals.value())
    dict([(3, 9), (4, 16), (5, 25)])
    numerals.get('A', 0)
    numerals.get('V', 0)

def tuple_demos():
    (3, 4, 5, 6)
    3, 4, 5, 6
    ()
    tuple()
    tuple([1, 2, 3])
    (2, )
    (3, 4) + (5, 6)
    (3, 4, 5) * 2
    5 in (3, 4, 5)

    # {[1]: 2}
    {1: [2]}
    {(1, 2): 3}
    # {([1], 2): 3}
    {tuple([1, 2]): 3}

def divide_exact(n, d):
    return n // d, n % d

def identity_demos():
    a = [10]
    b = a
    a == b
    a is b
    a.extend([20, 30])
    a == b
    a is b

    a = [10]
    b = [10]
    a == b
    a is not b
    a.append(20)
    a != b
