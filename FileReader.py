#!/usr/bin/env python3

import sys #to get variables directly from command line

filename = sys.argv[1] #the file to be opened is specfied through the command line

with open(filename) as f: #opens file

	for line in f:	#iterates through lines in the file

		print(line) #prints each line
