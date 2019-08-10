#!/usr/local/bin/python3

#############################################################################################
#                               Program by Mohammed Faisal Khan                             #
#                               Email: faisalkhan91@outlook.com                             #
#                               Date: 8/10/2019                                             #
#############################################################################################

# Importing system module

import random
import math


def mean (numbers, num):
	sum = 0

	for val in numbers:
		sum += val

	return sum / num


def stddev (numbers, mean, num):
	sum = 0

	for val in numbers:
		sum += (val - mean) ** 2

	return math.sqrt(sum / num)


def median (numbers, num):

	numbers.sort()
	return numbers[num // 2]


def mode (numbers, num):
	modval = []
	modcount = 0
	index = 0

	while index < num :
		c = 1
		while index+c < num and numbers[index] == numbers[index+c] :
			c += 1

		if c == modcount:
			modval.append(numbers[index])
		elif c > modcount:
			modcount = c
			modval = [numbers[index]]
		index += c

	return modval


def getsample (numbers, num):
	i = 0
	while i < num :
		sample = random.normalvariate(75, 50)
		numbers.append(int(sample))
		i += 1
	

random.seed()

for n in [100, 1000, 10000, 100000, 1000000]:
	samples = []
	getsample(samples, n)
	print("N =", n)
	avg = mean(samples, n)
	print("Avg =", avg)
	std = stddev(samples, avg, n)
	print("Std =", std)
	med = median(samples, n)
	print("Median = ", med)
	mod = mode(samples, n)
	print("Mode =", mod)
	#print("N =", n, "Avg =", avg, "Std =", std, "Median =", med, "Mode =", mod)


#############################################################################################
#                                       End of Program                                      #
#                                       Copyright 2019                                      #
#############################################################################################



