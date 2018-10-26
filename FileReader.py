import sys

filename = sys.argv[1]

with open(filename) as f:

	for line in f:	

		print(line)
