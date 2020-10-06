def multiply(a, b):

    if b == 1:  # base case
        return a
    elif b == 0:
        return 0
    elif b == -1:
        return a * -1
    # ex 2 * (-3) = -2 - 2 - 2
    #    - 6 = - 6
    elif b < -1:
        return (a - multiply(a, b + 1)) * -1
    # recursive case
    return a + multiply(a, b - 1)
