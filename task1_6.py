#!/usr/bin/python

import itertools
import time

def change_list(l):
	if isinstance(l, list):
		l = [list_item + 1 for list_item in l]
		return l
	return "Parametr is not a list"

def change_list_by_if(l):
	if isinstance(l, list):
		l = [list_item + 1 for list_item in l if list_item % 2]
		return l
	return "Parametr is not a list"

def two_lists(first_list, second_list):
	if isinstance(first_list and second_list, list):
		l = [second for first in first_list for second in second_list]
		return l
	return "Parametr is not a list"

def change_list_generator(l):
	if isinstance(l, list):
		for item in l:
			yield item + 1	

def change_list_by_if_generator(l):
	if isinstance(l, list):
		for item in l:
			if item % 2:
				yield item + 1	

def itertools_count(start, step):
	if isinstance(start and start, int):
		for item in itertools.count(start=start, step=step):
			print item
			if item > 1000:
				break 
	return "Parametrs is not int"

def itertools_combinations(i, r):
	if isinstance(i, str) and isinstance(r, int):
		for item in itertools.combinations('ABCD', 2):
			print item
	return "Wrong Parametrs"

def itertools_combinations_with_replacement(i, r):
	if isinstance(i, str) and isinstance(r, int):
		for item in itertools.combinations_with_replacement('ABCD', 2):
			print item
	return "Wrong Parametrs"

def itertools_dropwhile(l):
	if isinstance(l, list):
		for item in itertools.dropwhile(lambda x: x < 5, l):
			print item
	return "Parametr is not a list"

def itertools_groupby(l):
	if isinstance(l, list):
		for key, group in itertools.groupby(l, lambda x: x[0]):
			for item in group:
				print("A %s is a %s." % (item[1], key))
		print ''
	return "Parametr is not a list"

# 2.a

def few_values():
	first_value = 'first_value'
	second_value = 'second_value'

	return first_value, second_value

# print few_values()

# 2.b

def generator(n):
	for i in n: 
		yield i*2

# print generator(xrange(100))

#2.c

def lambda_function(n):
	return map(lambda x: x * 2, n)

# print lambda_function(xrange(100))

def listgen_func(n):
	return [i * 2 for i in n]

print listgen_func(xrange(100))

# *args, **kwargs, otional и named
def args_func(*args):
	return args

print args_func(1, 2, 3)

def kwargs_func(**kwargs):
	return kwargs

print kwargs_func(first_arg = 123, second_arg = 'second')

# decorator: work tme of function
def func_timer_decorator(func):
	def wrapper():
		func_start = time.time()
		func()
		func_stop = time.time()
		print 'Worktime of function: %s' % (func_stop - func_start)
		return func()

	return wrapper

@func_timer_decorator
def time_of_function():
	return "func_timer_decorator"


# decorator: name of function befor start
def name_of_func_decorator(func):
	def wrapper():
		print "Name of function is: '%s'" % func.func_name
		return func()
	return wrapper

@name_of_func_decorator
def my_name_is_first_function():
	return "First function"

# decorator: user check
import getpass
USER = 'another_user'

def check_user_decorator(func):
	def wrapper():
		if getpass.getuser() != USER:
			pass	
		else:
			return func()
	return wrapper

@check_user_decorator
def user_check():
	print "user check"

# decorator: decorator with exception
def decoartor_with_exception(func):
	def wrapper():
		if func() is True:
			pass
		else:
			class CustomException(Exception):
				def __init__(self, message, errors):
					super(CustomException, self).__init__(message)
			raise CustomException(func(), 200)
	return wrapper			

@decoartor_with_exception
def exception_func():
	return "string for check"

# print change_list([1, 2, 3])

# print change_list_by_if([1, 2, 3])

# print two_lists(['one', 'two', 'three'], [1, 2, 3, 4], )

# print change_list_generator([1, 2, 3, 4])

# print change_list_by_if_generator([1, 2, 3, 4])

# print itertools_count(2, 5)

# print itertools_combinations('ABCD', 2)

# print itertools_combinations_with_replacement('ABCD', 2)

# print itertools_dropwhile([1,4,6,4,1])

# print itertools_groupby([
# 	("animal", "bear"), 
# 	("animal", "duck"), 
# 	("plant", "cactus"),
# 	("vehicle", "speed boat"), 
# 	("vehicle", "school bus")
# ])

print 

# print time_of_function()

# print my_name_is_first_function()

# print user_check()

# print exception_func()