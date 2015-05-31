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

def combine_dict(first_dict, second_dict):
	if isinstance(first_dict and second_dict, dict):
		for key in first_dict.keys():
			if second_dict.has_key(key):
				del second_dict[key]
		first_dict.update(second_dict)

		return first_dict		
	return "Parameters is not a dict"

def calc(operation, first_arg, second_arg):
	if isinstance(operation, str) or isinstance(first_arg and second_arg, int):

		operation_dict = {
			"plus": first_arg + second_arg, 
			"minus": first_arg - second_arg, 
			"multiply": first_arg * second_arg,
			"division": first_arg / second_arg
		}

		return operation_dict[operation]
	return "Wrong parameters"

def switch_dict(dictionary):
	if isinstance(dictionary, dict):
		result_dictionary = {}

		for key, value in dictionary.iteritems():
			result_dictionary[value] = key

		return result_dictionary
	return "Parameter is not a dict"

# print

# print a_make_dict(['my', 'first', 'dict'], [1, 2, 3])

# print b_make_dict([('my', 1), ('first', 2), ('dict', 3)])

# print dict_and_letter({'one': 1, 'two': 2, 'three': 3}, 'three')

# print combine_dict({"1":"one", "2":"two", "3":"three"}, {"1":"one", "2":"two", "4":"four"})

# print calc("plus", 5, 5)

print switch_dict({1: "one", 2: "two", 3: "three", 4: "four"})
