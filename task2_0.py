#!/usr/bin/python

#1.a
class OldStyleClass():
    pass

class NewStyleClass(object):
	pass

class AnotherNewStyleClass(NewStyleClass):
	pass

# 1.b 
class ClassWithConstructor(object):
	def __init__(self, first_arg, second_arg):
			# Автоматически задаем значения атрибутам класса при его создании.
			self.first_arg = 'first'
			self.second_arg = 'second'
