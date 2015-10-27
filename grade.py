# grade.py
#
# Calculate grade A to F base on score 0.0 - 1.0

try:
    score = raw_input('Enter score: ')
    s = float(score)
except:
    print('Please enter only number')
    
if s > 1.0 :
    print 'Please enter in range of 0.0 - 1.0'
    quit()
    
if s >= 0.9 :
    print 'A'
elif s >= 0.8 :
    print 'B'
elif s >= 0.7 :
    print 'C'
elif s >= 0.6 :
    print 'D'
else:
    print 'F'
