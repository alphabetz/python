# mailcount.py
#
# count mail

fname = open('mbox-short.txt')
counts = dict()
for line in fname:
    words = line.split()
    for word in words:
        wrd = word.lower()
        #get value or create if no exist
        counts[wrd] = counts.get(wrd, 0) + 1

lst = list()

for key, value in counts.items():
    lst.append( (value, key) )
lst.sort(reverse=True)

for value, key in lst[:10]:
    print key, value
