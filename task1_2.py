#!/usr/bin/python
import random

def letters(big_string):
	if isinstance(big_string, str):
		return big_string.upper()
	return "Received is not a string"

def palindrome(pali):
	for i, letter in enumerate(pali):
		if letter != pali[-i-1]:
			return "String is not a palindrome"
	return "String is a palindrome"

def find_letter(where, letter):
    if isinstance(where, str) and isinstance(letter, str):
    	where = where.split()
    	words_on_letter = [word for word in where if word[0].lower() == letter]
    	return words_on_letter
	return "Parametrs is not a string"

def mix_words(just_string):
	if isinstance(just_string, str):
		just_string_list = just_string.split()
		random.shuffle(just_string_list)
		return just_string_list
	return "Received is not a string"

print letters("Trees Are So Kind")

print palindrome("avid diva")

print find_letter("Bears are the best animals ever", 'b')

print mix_words("Bears are the best animals ever")
