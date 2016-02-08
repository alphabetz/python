def isPalindrome(s):
    '''
    This called 'Divide and Conquer algorithm'
    '''
    def toChar(s):
        return s.replace(' ', '').lower() # lower and trim all spaces
        
    def isPal(s):
        if len(s) <= 1:
            return True
        else:
            return s[0] == s[-1] and isPalindrome(s[1:-1])
            
    return isPal(toChar(s))
