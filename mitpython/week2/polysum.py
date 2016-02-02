from math import *

def polysum(n, s):
    """    
    polysum takes 2 arguments, n and s. This function should sum the area
    and square of the perimeter of the regular polygon. The function returns
    the sum, rounded to 4 decimal places.
    """
    area = (0.25 * n * (s ** 2)) / tan(pi / n)
    perimeter = n * s
    return round(area + (perimeter ** 2), 4)
