def recurl_mul(a, b):
    '''
    Recursive version of basic multipication of numbers
    the idea is a * b = a + a + a ... + a in b times
    so we will keep addition until b = 1
    therefore, a * b = a + a * (b - 1)
    '''
    if b == 1:
        return a
    else:
        return a + recurl_mul(a, b-1)

def recurl_factorial(n):
    ''''
    Recursive for factorial with formula of n * (n - 1)
    '''
    if n == 1:
        return n
    else:
        return n * recurl_factorial(n-1)
