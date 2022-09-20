def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


# Ordering

def cascade(n):
    """Print a cascade of prefixes of n."""
    if n < 10:
        print(n)
    else:
        print(n)
        cascade(n // 10)
        print(n)


def cascade2(n):
    """Print a cascade of prefixes of n."""
    print(n)
    if n >= 10:
        cascade(n // 10)
        print(n)


def inverse_cascade(n):
    """Print an inverse cascade of prefixes of n."""
    grow(n)
    print(n)
    shrink(n)


def f_then_g(f, g, n):
    if n:
        # if n not 0
        f(n)
        g(n)


grow = lambda n: f_then_g(grow, print, n//10)
shrink = lambda n: f_then_g(print, shrink, n//10)


# Tree Recursion
def fib(n):
    """Compute the nth Fibonacci number."""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)


# Hanoi Tower
def print_move(disk, origin, destination):
    """Print instructions to move a disk."""
    print("Move disk " + str(disk) + " from " + str(origin) + " to " + str(destination))


def move_stack(n, start, end):
    """Print the moves required to move n disks on the start pole to the end pole
    without violating the rules of Towers of Hanoi.

    n -- number of disks
    start -- a pole position, either 1, 2, or 3
    end -- a pole position, either 1, 2, or 3

    There are exactly three poles, and start and end must be different.
    Assume that the start pole has at least n disks of increasing size,
    and the end pole is either empty or has a top disk larger then the top n start disks.
    """
    assert 1 <= start <= 3 and 1 <= end <= 3 and start != end, "Bad start/end"
    if n == 1:
        print_move(n, start, end)
    else:
        spare_peg = 6 - start - end
        move_stack(n - 1, start, spare_peg)
        print_move(n, start, end)
        move_stack(n - 1, spare_peg, end)

        
# count partitions
def count_partitions(n, m):
    """Count the partitions of n using parts up to size m."""

    if n == 0:
        return 1
    elif n < 0:
        return 0
    elif m == 0:
        return 0
    else:
        with_m = count_partitions(n - m, m)
        without_m = count_partitions(n, m - 1)
        return with_m + without_m
