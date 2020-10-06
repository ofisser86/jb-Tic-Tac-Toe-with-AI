def fib(n):

    if n == 0:  # base case for month 0
        return n  # the rabbits are not on a farm yet!
    elif n == 1:  # base case for month 1
        return n  # a pair of baby rabbit has just arrived!
    else:
        return fib(n - 1) + fib(n - 2)   # recursive calls
