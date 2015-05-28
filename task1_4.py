#!/usr/bin/python

def dict_methods():
	pass

def a_make_dict(first_list, second_list):
	if isinstance(first_list and second_list, list):
		return dict(zip(first_list, second_list))

def b_make_dict(first_list):
	if isinstance(first_list, list):
		return dict(first_list)

def dict_and_letter(dictionary, letter):
	if isinstance(dictionary, dict):
		dictionary[letter] = None
		return dictionary

# print

# print a_make_dict(['my', 'first', 'dict'], [1, 2, 3])

# print b_make_dict([('my', 1), ('first', 2), ('dict', 3)])

print dict_and_letter({'one': 1, 'two': 2, 'three': 3}, 'three')