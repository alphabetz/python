def totalDiff(senA, senB, size):
    '''
    Two sensor with same size of data but a little different
    find the differences
    '''
    # first write iterative function to solve the problem
    total = []
    for i in range(size):
        total.append(abs(senA[i] - senB[i]))
    
    return sum(total)

# Write dispathcer function to solve minimal data set
# and call iterative function to solve data not minimal

def totalDispatcher(senA, senB, size):
    if size == 0: return 0
    lastElement = abs(senA[size - 1] - senB[size - 1])
    diff = totalDiff(senA, senB, size - 1) + lastElement
    
    return diff

# Change dispathcer that called iterative function to call it self
def totalDifferent(senA, senB, size):
    if size == 0: return 0
    lastElement = abs(senA[size - 1] - senB[size - 1])
    
    return totalDifferent(senA, senB, size - 1) + lastElement

# Multipication
def multiIter(a,b):
    total = 0
    for i in range(b):
        total += a
    return total

def multiCurl(a, b):
    if b == 1: return a
    
    return a + (multiCurl(a, b - 1))
#######################################

# Factorial
# Step 1 iterative function
def factorial(n):
    fact = 1
    while n > 0:
        fact *= n
        n -= 1
    
    return fact
    
# Step 2 dispatcher
def factorialDis(n):
    if n == 1: return n
    #return n * factorial(n - 1)
    # Step 3 call itself
    return n * factorialDis(n - 1)
        