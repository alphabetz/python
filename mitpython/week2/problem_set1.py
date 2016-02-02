def count_vowels(s):
    """
    Assume s is a string of lower case characters.
    Write a program that counts up the number of vowels contained in the string
    s. Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. For example, if s =
    'azcbobobegghakl', your program should print:
    """
    s = s.lower()
    count = 0
    vowels = ['a', 'e', 'i', 'o', 'u']
    for char in s:
        if char in vowels:
            count += 1
    print "Number of vowels: " + str(count)

def count_bob(s):
    """
    Write a program that prints the number of times the string 'bob' occurs in s.
    """
    count = 0
    for i in range(1, len(s) - 1):
        if s[i - 1:i + 2] == 'bob':
            count += 1

def item_order(order):
    water = 0
    salad = 0
    hamburger = 0
    order = order.split()
    for i in order:
        if i == 'salad':
            salad += 1
        if i == 'water':
            water += 1
        if i == 'hamburger':
            hamburger += 1
    print "salad:" + str(salad) + " hamburger:" + str(hamburger) + " water:" + \
    str(water)
            
    
    
    
    
    
    
    
    