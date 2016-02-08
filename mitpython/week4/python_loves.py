def nfruits(dictionary_fruits, pattern_fruits) :
    assert len(dictionary_fruits) < 10
    for x in pattern_fruits :
        if x in dictionary_fruits.keys() :
            # if x is last element in dict break
            #if x == dictionary_fruits.keys()[-1]:
                #break
            dictionary_fruits[x] -= 1
            print 'in for x loop ', dictionary_fruits
        for y in dictionary_fruits.keys() :
            if y != x :
                dictionary_fruits[y] += 1
                print 'in for y loop ', dictionary_fruits
    return max(dictionary_fruits.values())

print nfruits({'A': 1, 'B': 2, 'C': 3}, 'AC')
