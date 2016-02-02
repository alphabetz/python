def min_pay(balance, annualInterestRate, monthlyPaymentRate):
    monthly_interate = annualInterestRate / 12.0
    total_paid = 0
    for i in range(1, 13):
        minimum_payment = monthlyPaymentRate * balance
        month_unpaid = balance - minimum_payment
        balance = month_unpaid + (monthly_interate * month_unpaid)
        total_paid += minimum_payment    
        # output
        print "Month: " + str(i) + "\n"
        print "Minimum monthly payment: %.2f" %(minimum_payment) + "\n"
        print "Remaining balance: %.2f" %(balance) + "\n" 
    print "Total paid: %.2f" %(total_paid) + "\n"
    print "Remaining balance: %.2f" %(balance)

def fixed_pay(balance, annualInterestRate):
    cur_balance = balance
    monthly_interest = annualInterestRate / 12
    payment = 0
    increment = 10
    while (cur_balance > 0):
        cur_balance = balance
        payment += increment
        for month in range(12):
            unpaid = cur_balance - payment
            cur_balance = unpaid + (unpaid * monthly_interest)


    print 'Lowest Payment: ' + str(payment)

def bisection_pay(balance, annualInterestRate):
    original_balance = balance
    original_interest = annualInterestRate
    lowerbound = balance / 12
    upperbound = (balance * (1 + annualInterestRate / 12) ** 12) / 12.0
    payment = (lowerbound + upperbound) / 2
    while True:
        for i in range(1, 13):
            unpaid = balance - payment
            balance = unpaid + (unpaid * annualInterestRate / 12.0)
        if (abs(balance - 0)) < 0.1:
            print "Lowest payment: ", round(payment, 2)
            break
        else:
            if balance < 0:
                upperbound = payment
            elif balance > 0:
                lowerbound = payment
        payment = (lowerbound + upperbound) / 2
        balance = original_balance
        annualInterestRate = original_interest
        
    