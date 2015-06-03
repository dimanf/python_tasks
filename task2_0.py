#!/usr/bin/python
# coding: utf-8

#1.a
class OldStyleClass():
    pass

class NewStyleClass(object):
	pass

class AnotherNewStyleClass(NewStyleClass):
	pass

class ClassWithConstructor(object):
	def __init__(self, *args):
			# Автоматически задаем значения атрибутам класса при его создании.
			if args:
				self.first_arg = args[0]
				self.second_arg = args[1]

	@staticmethod
	def smethod(first_arg, second_arg):
		return first_arg + second_arg

	@classmethod
	def cmethod(cls):
		return cls.__name__

	@property
	def cls_name(self):
		return self.first_arg, self.second_arg

class_with_staticmethod = ClassWithConstructor.smethod(1, 2)
class_with_classmethod = ClassWithConstructor.cmethod()
class_with_property = ClassWithConstructor('farg', 'sarg')

# print class_with_staticmethod
# print class_with_classmethod
# print class_with_property.cls_name
