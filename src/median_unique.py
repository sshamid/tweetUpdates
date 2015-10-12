#Calculate the median number of unique words per tweet, and update this median as tweets come in

import sys

input_file = open(sys.argv[1], 'r')
output2 = open(sys.argv[2], 'w')

def RunningMedian(f):
	# initializing line number counts
    running_line_number = 0.
    # initializing running total unique word counts 
    running_unique_words = 0
    
    # reading each line from the file
    for line in f:
        # remove leading and trailing whitespace
        line = line.strip()
        # increment line count
        running_line_number += 1
        # split the line into words
        words = line.split()
        # construct unique words for each line         
        uniquewords = set(words)
        # running total words considering only unique words per tweet
        running_unique_words += len(uniquewords)
        # calc median
        running_median = (running_unique_words/running_line_number)
        # write result to a file    
        output2.write('{0:.2f}'.format(running_median) + '\n')
    
    # closing file
    output2.close()

RunningMedian(input_file)