def recurPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    if exp == 1:
        return base
    elif exp == 0:
        return 1
    else:
        return base * recurPower(base, exp - 1)

def recurPowerNew(base, exp):
    '''
    base: int or float.
    exp: int >= 0

    returns: int or float; base^exp
    '''
    # Your code here
    if exp == 0:
        return 1
    elif exp & 1: # even case (& operation return 0 in case even number)
        return recurPowerNew(base * base, exp / 2)
    else:
        return base * recurPowerNew(base, exp - 1)
def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    divisor = min(a, b)
    while divisor > 1 and (a % divisor != 0 or b % divisor != 0):
        divisor -= 1
    return divisor

def gcdRecur(a, b):
    if b == 0:
        return a
    else:
        return gcdRecur(b, a % b)

# L5_problems 6
# Write an iterative function, lenIter, 
# which computes the length of an input argument (a string), 
# by counting up the number of characters in the string.
def lenIter(aStr):
    length = 0
    for char in aStr:
        length += 1
    return length

def lenRecur(aStr):
    if aStr == '':
        return 0
    else:
        return 1 + lenRecur(aStr[:-1])

def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    if aStr=="":
        return False
    else:
        n=len(aStr)
        if char==aStr[n/2]:
            return True
        elif char>aStr[n/2]:
            return isIn(char,(aStr[(n/2)+1:]))
        else:
            return isIn(char,(aStr[:(n/2)]))
    
def semordnilapWrapper(str1, str2):
    # A single-length string cannot be semordnilap
    if len(str1) == 1 or len(str2) == 1:
        return False

    # Equal strings cannot be semordnilap
    if str1 == str2:
        return False

    return semordnilap(str1, str2)

def semordnilap(str1, str2):
    '''
    str1: a string
    str2: a string
    
    returns: True if str1 and str2 are semordnilap;
             False otherwise.
    
    '''
    #base case
    if len(str1) != len(str2):
        return False
    if len(str1) == 1: 
        return str1[0] == str2[-1]
    else:
        print 'first char of current str1[0]=',str1[0]
        print 'last char of current str2[-1]=',str2[-1]
        print 'str1=',str1[1:]
        print 'str2=',str2[:-1]
        return str1[0] == str2[-1] and semordnilap(str1[1:], str2[:-1])