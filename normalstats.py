#!/usr/local/bin/python3


#############################################################################################
#                               Program by Mohammed Faisal Khan                             #
#                               Email: faisalkhan91@outlook.com                             #
#                               Date: 8/9/2019                                              #
#############################################################################################

# Importing system module

import random
import math


def mean(numbers):
	sum = 0

	for i in range(0, len(numbers)):
		sum += numbers[i]

	return sum / len(numbers)


def stddev(numbers, mean, num):
	sum = 0

	for i in range(0, num):
		sum += (numbers[i] - mean) ** 2

	return math.sqrt(sum / num)	


def median(numbers):

	numbers.sort()
	return numbers[len(numbers) // 2]


def mode(numbers):
	modval = 0
	modcount = 0
	index = 0

	while index < len(numbers):
		c = numbers.count(numbers[index])
		if c > modcount:
			modcount = c
			modval = numbers[index]
		index += c

	return modval


def getsample(numbers, num):
	for i in range(0, num):
		sample = random.normalvariate(75, 50)
		numbers.append(int(sample))
	

random.seed()

for n in [100, 1000, 10000, 100000, 1000000]:
	samples = []
	getsample(samples, n)
	avg = mean(samples)
	std = stddev(samples, avg, n)
	med = median(samples)
	mod = mode(samples)
	print("N =", n, "Avg =", avg, "Std =", std, "Median =", med, "Mode =", mod)

#############################################################################################
#                                       End of Program                                      #
#                                       Copyright 2019                                      #
#############################################################################################
