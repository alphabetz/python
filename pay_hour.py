# pay_hour.py
#
# Calculate pay hours base on 10.50 per hour and 1.5 times if more than 40 hours

try:
    hrs = raw_input('Enter hour(s): ')
    h = float(hrs)
    rate = raw_input('Enter rate: ')
    r = float(rate)
    extra_h = 15.75
except:
    print 'Error please enter only number'
    quit()

if h > 40 :
    extra_pay = (h - 40) * extra_h
else:
    extra_pay = 0

gross_pay = 40 * r + extra_pay

print gross_pay
