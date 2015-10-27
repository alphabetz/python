#!/usr/bin/python2.7
# pocket.py
#
# Gen XKCD password

import random

word_file = open('pocket.txt', 'r')
word_list = word_file.readlines()

for i in range(5):
    pwlist = []
    for j in range(4):
        rand_word = word_list[random.randrange(len(word_list))]
        rand_word = rand_word[:-1]
        pwlist.append(rand_word)
        pw = "".join(pwlist)
        pw = pw.replace('e', '3')
        pw = pw.replace('o', '0')
        print(len(pw), pw)


