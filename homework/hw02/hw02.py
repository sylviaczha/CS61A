def next_smallest_coin(coin):
    if coin == 25:
        return 10
    elif coin == 10:
        return 5
    elif coin == 5:
        return 1


def start_coin(coin):
    if coin >= 25:
        return 25
    elif coin >= 10:
        return 10
    elif coin >= 5:
        return 5
    else:
        return 1


def count_coins(total):
    """Return the number of ways to make change for total using coins of value of 1, 5, 10, 25.
    >>> count_coins(15)
    6
    >>> count_coins(10)
    4
    >>> count_coins(20)
    9
    >>> count_coins(100) # How many ways to make change for a dollar?
    242
    >>> from construct_check import check
    >>> # ban iteration
    >>> check(HW_SOURCE_FILE, 'count_coins', ['While', 'For'])
    True
    """
    "*** YOUR CODE HERE ***"
    
    def helper(total, n):
        if total < 0:
            return 0
        elif total == 0:
            return 1
        elif n == 1:
            return 1
        else:
            return helper(total - n, n) + helper(total, next_smallest_coin(n))
    return helper(total, start_coin(total))

print(count_coins(100))
