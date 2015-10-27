# file_read.py
#
# Read file user input and print it all uppercase

fname = raw_input("Enter file name: ")
fh = open(fname)

for i in fh:
    i = i.strip().upper()
    print i
