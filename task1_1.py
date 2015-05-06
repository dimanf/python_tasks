#!/usr/bin/python
import math 

def multipliers(number):

	rez = '1'
	while number % 2 == 0:
		rez += " * 2"
		number = number / 2
	i = 3
	while i <= number:
		if number % i == 0:
			rez += " * " + str(i)
			number = number / i
		else:
			i +=2
	return rez

def equation(a, b, c):
	d = b*b-4*a*c
	x1 = 0
	x2 = 0
	if d == 0:
		x1 = (-1*b)/(2*a)
		return "x = " + str(x1)
	elif d > 0:
		x1 = (-1*b + math.sqrt(d))/(2*a)
		x2 = (-1*b - math.sqrt(d))/(2*a)
		return "x1 = " + str(x1) + "; x2 = " + str(x2)
	else:
		return "no result"


def simple(number):
	for i in xrange(2,number-1):
		if not number % i:
			return False
	return True

# # atm uses only 100, 50, 20, 10, 5 and 1 notes.
def atm(summ):


#print multipliers(12)

#print equation(2, 19, 35) # 2x^2 + 19x + 35 = 0

print simple(14)

# print atm(287)
