HW_SOURCE_FILE=__file__


def num_eights(x):
    """Returns the number of times 8 appears as a digit of x.

    >>> num_eights(3)
    0
    >>> num_eights(8)
    1
    >>> num_eights(88888888)
    8
    >>> num_eights(2638)
    1
    >>> num_eights(86380)
    2
    >>> num_eights(12345)
    0
    >>> from construct_check import check
    >>> # ban all assignment statements
    >>> check(HW_SOURCE_FILE, 'num_eights',
    ...       ['Assign', 'AugAssign'])
    True
    """
    "*** YOUR CODE HERE ***"
    if x == 0:
        return 0
    else:
        if x % 10 == 8:
            return 1 + num_eights(x // 10)
        else:
            return num_eights(x // 10)


def pingpong(n):
    """Return the nth element of the ping-pong sequence.

    >>> pingpong(8)
    8
    >>> pingpong(10)
    6
    >>> pingpong(15)
    1
    >>> pingpong(21)
    -1
    >>> pingpong(22)
    -2
    >>> pingpong(30)
    -2
    >>> pingpong(68)
    0
    >>> pingpong(69)
    -1
    >>> pingpong(80)
    0
    >>> pingpong(81)
    1
    >>> pingpong(82)
    0
    >>> pingpong(100)
    -6
    >>> from construct_check import check
    >>> # ban assignment statements
    >>> check(HW_SOURCE_FILE, 'pingpong', ['Assign', 'AugAssign'])
    True
    """
    "*** YOUR CODE HERE ***"
    def helper(index, ppn, dir):
        if index == n:
            return ppn
        elif index % 8 == 0 or index % 10 == 8:
            return helper(index + 1, ppn - dir, -dir)
        else:
            return helper(index + 1, ppn + dir, dir)
    return helper(1, 1, 1)


# interative solution
def pingpong2(n):
    index, ppn, dir = 1, 1, 1
    while index != n:
        index += 1
        ppn += dir
        if index % 8 == 0 or index % 10 == 8:
            dir = - dir
    return ppn

# a helper function is helpful when having extra values to keep track of
# a helper function is the mirror image of what the while loop is doing
# each recursive framework is going to be a single while loop
