from math import sqrt
from numpy import dot, array

def euclid_dist(p1, p2):
	euclid_sum = 0
	for i,j in zip(p1, p2):
		euclid_sum += math.sqrt((j - i) ** 2)
	return euclid_sum

def np_euclid_dist(p1, p2):
    np1, np2 = array(p1), array(p2)
    return sqrt(dot(np2 - np1, np2 - np1))

def manhattan_dist(p1, p2):
    manhattan_sum = 0
    for i, j in zip(p1 ,p2):
        manhattan_sum += abs(i - j)
    return manhattan_sum

def np_manhattan_dist(p1 ,p2):
    np1, np2 = array(p1), array(p2)
    return dot(abs(np2 - np1), 1).sum()
