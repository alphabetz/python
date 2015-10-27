import random

def generator(num):
    list = []
    for i in range(1,num):
      list.append(i)
    random.shuffle(list)
    return list
