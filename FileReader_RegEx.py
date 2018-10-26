import sys
import re

matchString = ""

with open(sys.argv[1]) as f:

	for line in f:

		matchString += line

p = re.compile('.+(\w+).+:.(\w+).+.:.(\w+).+')
print(matchString)
