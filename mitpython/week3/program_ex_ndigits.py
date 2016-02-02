def ndigits(x):
    x = abs(x)
    if x < 10:
        return 1 # base case
    else:
        return ndigits(x / 10) + 1