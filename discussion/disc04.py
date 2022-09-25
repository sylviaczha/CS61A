"""1.1"""
def count_stair_ways(n):
    if n == 0 or n == 1:
        return 1
    else:
        return count_stair_ways(n - 1) + count_stair_ways(n - 2)

"""1.2"""
def count_k(n, k):
    if n == 0:
        return 1
    elif n < 0:
        return 0
    else:
        total = 0
        i = 1
        while i <= k:
            total += count_k(n - i, k)
            i += 1
        return total

"""2.2"""
def even_weighted(s):
    return [i * s[i] for i in range(len(s)) if i % 2 == 0]

"""2.3"""
def max_product(s):
    """Return the maximum product that can be formed using
    non-consecutive element of s."""
    if s == []:
        return 1
    elif len(s) == 1:
        return s[0]
    else:
        return max(max_product(s[1:]), s[0] * max_product(s[2:]))
