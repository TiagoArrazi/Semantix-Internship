#!/usr/bin/env python3

import sys
import re #to use regular expressions

matchString = "" #this will be the string that will receive the content inside the file to be read

with open(sys.argv[1]) as f: #opens file

	for line in f: #iterates through each line in file

		matchString += line #

p = re.compile('.+(\w+).+:.(\w+).+.:.(\w+).+')
print(matchString)
