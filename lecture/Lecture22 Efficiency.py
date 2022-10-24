def fib(n):
    """The nth Fibonacci number."""
    if n == 0 or n == 1:
        return n
    else:
        return fib(n-2) + fib(n-1)


# Time
def count(f):
    """Return a counted version of f with a call_count attribute."""
    def counted(*args):
        counted.call_count += 1
        return f(*args)
    counted.call_count = 0
    return counted


# Memoization
def memo(f):
    """Memoize f."""
    cache = {}
    def memoized(n):
        if n not in cache:
            cache[n] = f(n)
        return cache[n]
    return memoized


# Space
def count_frames(f):
    """Return a counted version of f with a max_count attribute."""
    def counted(n):
        counted.open_count += 1
        counted.max_count = max(counted.max_count, counted.open_count)
        result = f(n)
        counted.open_count -= 1
        return result
    counted.open_count = 0
    counted.max_count = 0
    return counted


# Order of growth
def exp(b, n):
    """Return b to the n."""
    if n == 0:
        return 1
    else:
        return b * exp(b, n-1)


def square(x):
    return x * x


def exp_fast(b, n):
    """Return b to the n."""
    if n == 0:
        return 1
    elif n % 2 == 0:
        return square(exp_fast(b, n//2))
    else:
        return b * exp_fast(b, n-1)


# Overlap
def overlap(a, b):
    """Count the number of items that appear in both a and b."""
    count = 0
    for item in a:
        for other in b:
            if item == other:
                count += 1
    return count
