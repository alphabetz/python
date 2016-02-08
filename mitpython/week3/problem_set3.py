def f(x):
    import math
    return 200*math.e**(math.log(0.5)/14.1 * x)

def radiationExposure(start, stop, step):
    '''
    Computes and returns the amount of radiation exposed
    to between the start and stop times. Calls the 
    function f (defined for you in the grading script)
    to obtain the value of the function at any point.
 
    start: integer, the time at which exposure begins
    stop: integer, the time at which exposure ends
    step: float, the width of each rectangle. You can assume that
      the step size will always partition the space evenly.
    returns: float, the amount of radiation exposed to 
      between start and stop times.
    '''
    if start >= stop - step:
        return f(start) * step
    else:
        return (f(start) * step) + radiationExposure(start+step, stop, step)

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    if len(secretWord) <= 1:
        return secretWord[0] in lettersGuessed
    else:
        return ((secretWord[0] in lettersGuessed) and
        isWordGuessed(secretWord[1:], lettersGuessed))

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    output = ""
    for i in secretWord:
        if i in lettersGuessed:
            output += i
        else:
            output += "_"
    return output

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    import string
    aval_letters = ""
    for letter in string.ascii_lowercase:
        if letter not in lettersGuessed:
            aval_letters += letter
    return aval_letters

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    print 'Welcome to the game, Hangman!'
    print 'I am thinking of a word that is ' + str(len(secretWord)) + ' letters long'
    print '------------- '
    
    i = 8
    lettersGuessed = []
    while i > 0 and '_' in getGuessedWord(secretWord, lettersGuessed):
        print 'You have ' + str(i) + ' guesses left.'
	print 'Available letters: ' + getAvailableLetters(lettersGuessed)
	guess = raw_input('Please guess a letter: ').lower()
	lettersGuessed.append(guess)
	if guess in secretWord:
	    if lettersGuessed.count(guess) > 1:
	        print "Oops! You've already guessed that letter: " + getGuessedWord(secretWord, lettersGuessed)
	    else:
	        print "Good guess: " + getGuessedWord(secretWord, lettersGuessed)
	else:
            if lettersGuessed.count(guess)>1:
                print "Oops! You've already guessed that letter: " + getGuessedWord(secretWord, lettersGuessed)
            else:
                print 'Oops! That letter is not in my word: ' + getGuessedWord(secretWord, lettersGuessed)
                i-=1
        print '------------'
	        
    if isWordGuessed(secretWord, lettersGuessed):
        return 'Congratulations, you won!'
    else:
        return 'Sorry, you ran out of guesses. The word was '+ secretWord + '.'
