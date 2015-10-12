#Calculate the total number of times each word has been tweeted

import sys
from collections import Counter

input_file = open(sys.argv[1], 'r')
output1 = open(sys.argv[2], 'w')

def WordCount(f):
    cnt = Counter()
    
    # reading lines from file
    for line in f:
        # remove leading and trailing whitespace
        line = line.rstrip()
        # split the line into words
        # also count and update words using counter object from python standard library
        cnt.update(x for x in line.split() if x)
    
    # write result to a file   
    for word, count in sorted(cnt.items()):
        output1.write('{0:30s} {1:d}'.format(word, count) + '\n')
    
    # closing file
    output1.close()

WordCount(input_file)
