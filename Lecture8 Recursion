def split(n):
"""Split a postive integer into all but its last digit and its last digit."""
    return n // 10, n % 10

def sum_digits(n):
"""Return the sum of the digits of positive integer n."""
    if n < 10:
        return n
    else:
        all_but_last, last = split(n)
        return sum_digits(all_but_last) + last

# Iteration vs Recursion
# Factorisation
def fact_iter(n):
    total, k = 1, 1
    while k <= n:
        total, k = total * k, k + 1
    return total

def fact_recur(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)

# Mutual Recursion
# Luhn Algorithm
def luhn_sum(n):
    """Return the digit sum of n computed by the Luhn algorithm."""
    if n < 10:
        return n
    else:
        all_but_last, last = split(n)
        return luhn_sum_double(all_but_last) + last

def luhn_sum_double(n):
    """Return the Luhn sum of n, doubling the last digit."""
    all_but_last, last = split(n)
    luhn_digit = sum_digits(2 * last)
    if n < 10:
        return luhn_digit
    else:
        return luhn_sum(all_but_last) + luhn_digit

# Converting recursion to iteration
def sum_digits(n):
    if n < 10:
        return n
    else:
        all_but_last, last = split(n)
        return sum_digits(all_but_last) + last

# Converting iteration to recursion
def sum_digits_iter(n):
    """Sum digits iteratively"""
    digit_sum = 0
    while  n > 0:
        n, last = split(n)
        digit_sum = digit_sum + last
    return digit_sum

def sum_digits_rec(n, digit_sum):
    if n == 0:
        return digit_sum
    else:
        n, last = split(n)
        return sum_digits_rec(n, digit_sum + last)
        
