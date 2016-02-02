#In this problem, you'll create a program that guesses a secret number!
#
#The program works as follows: you (the user) thinks of an integer between 0
#(inclusive) and 100 (not inclusive). The computer makes guesses, and you give
#it input - is its guess too high or too low? Using bisection search, the
#computer will guess the user's secret number!

low = 0
high = 100
count = 0
while True:
    print 'Please think of number between 0 and 100!'
    guess = (low + high) / 2
    count += 1
    print 'Is your magic number is ' + str(guess) + "?"
    ans = raw_input('Enter h to indicate the guess is too high. Enter l to indicate the guess is too low. Enter c   to indicate I guessed correctly.')
    if ans == 'c':
        if count <= 1:
            print "Game Over took " + str(count) + " guess"
        else:
            print "Game Over took " + str(count) + " guesses"
        print "Magic number is " + str(guess)
        break
    if ans == 'h':
        high = guess
    if ans == 'l':
        low = guess
