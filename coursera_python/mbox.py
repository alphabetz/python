# mbox.py
#
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# You will parse the From line using split() and print out the second word 
# in the line (i.e. the entire address of # # the person who sent the message). 
# Then print out a count at the end.
# Hint: make sure not to include the lines that start with 'From:'.

fh = raw_input("Name of file: ")
# 4
if '.txt' not in fh:
    fh = fh + '.txt'

f = open(fh)
count = 0

# this solution not work because they need us to made split()
'''
for line in f:
    line = line.rstrip()
    if line.startswith('From:'):
        print line[6:]
        count += 1
'''

# Let try another!

for line in f:
    line = line.rstrip() # for strip whitespace from right most
    if line.startswith('From'):
        if not line.startswith('From:'):
            line = line.split()
            print line[1]
            count += 1

print "There were", count, "lines in the file with From as the first word"

# 1. first solution doesn't work
# 2. second solution does work
# 3. damn fuck they need user input file name!
# 4. refactor to be handle user input
