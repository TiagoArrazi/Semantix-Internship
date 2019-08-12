from sys import argv


def hours_to_seconds(time_structure):
	h,m,s = tuple([int(e) for e in time_structure.split(':')])
	return h*3600 + m*60 + s
    


print(hours_to_seconds(argv[1]))

