def palindrome(s):
    '''
    1. write iterative function to solve the problem
    Was it a car or a cat I saw
    '''
    def toChar(s):
        return s.replace(' ', '').lower()
    
    def check(s):
        for char in s:
            for rechar in range(len(s) - 1, -1, -1):
                return char == s[rechar]
    
    #return check(toChar(s))
    '''
    2.Write dispatcher function too solve minimal data and call iterative function
      for non-minimal data can't think now
    '''
    