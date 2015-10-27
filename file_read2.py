# file_read2.py
#
# Search for specific text in file, extract it float number and calculate
# the average
# Use the file name mbox-short.txt as the file name

fname = raw_input("Enter file name: ")
fh = open(fname)
count = 0
new_x = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    new_x += float(line[20:])
    count += 1
    
print "Average spam confidence:", new_x / count
