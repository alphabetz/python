# tiny_pos.py
#
# sum all money

class bcolors:
        OKGREEN = '\033[92m'
        ENDC = '\033[0m'

total = 0
while True:
    try:
        product, quatity = raw_input('Number and price : ').split()
        product, quatity = [int(product), int(quatity)]
        total += product * quatity
        print bcolors.OKGREEN + "Summation is %d" %(product * quatity) +\
        bcolors.ENDC 
        print  bcolors.OKGREEN + "Total is now %d" %total + bcolors.ENDC
    except ValueError:
        print bcolors.OKGREEN + "Total %d" %total + bcolors.ENDC
        quit()
