# pay.py
#
# Calculate pay hours base on 10.50 per hour and 1.5 times 
# if more than 40 hours
# This time use function

def computepay(h, r):
    extra_h = 15.75
    if h > 40 :
        extra_pay = (h - 40) * extra_h
    else:
        extra_pay = 0
    gross_pay = 40 * r + extra_pay

    return gross_pay
    
hrs = raw_input('Enter hour(s): ')
h = float(hrs)
rate = raw_input('Enter rate: ')
r = float(rate)
    
