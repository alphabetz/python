# loop.py
#
#Once 'done' is entered, print out the largest and smallest of the numbers. If the user enters anything other than a #valid number catch it with a try/except and put out an appropriate message and ignore the number. Enter the numbers #from the book for problem 5.1 and Match the desired output as shown.


largest = None
smallest = None

while True:
    try:
        num = raw_input('Enter num: ')
        if num == 'done':
            break
        n = int(num)
        if largest < num or largest == None:
            largest = num
        if smallest > num or smallest == None:
            smallest = num
    except:
        print 'invalid input'

print "Maximum is", largest
print "Minimum is", smallest
        
    
    
