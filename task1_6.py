#!/usr/bin/python

import itertools

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

# print change_list([1, 2, 3])

# print change_list_by_if([1, 2, 3])

# print two_lists(['one', 'two', 'three'], [1, 2, 3, 4], )

# print change_list_generator([1, 2, 3, 4])

# print change_list_by_if_generator([1, 2, 3, 4])

# print itertools_count(2, 5)

# print itertools_combinations('ABCD', 2)

# print itertools_combinations_with_replacement('ABCD', 2)

# print itertools_dropwhile([1,4,6,4,1])

print itertools_groupby([
	("animal", "bear"), 
	("animal", "duck"), 
	("plant", "cactus"),
	("vehicle", "speed boat"), 
	("vehicle", "school bus")
])