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

class HtmlGenerator(object):

	@staticmethod
	def build_html(lines):
		lvl = -1
		t = re.compile('\t')
		stack = []
		dom = []
		for line in lines:
			tab_count =	len(t.findall(line))
			if tab_count > lvl:
				dom.append("\t"*tab_count + "<"+line[tab_count:-1]+">")
				stack.append(line[tab_count:-1])	
			elif tab_count == lvl:
				dom.append("\t"*tab_count + "</"+stack.pop()+">")
				dom.append("\t"*tab_count + "<"+line[tab_count:-1]+">")
				stack.append(line[tab_count:-1])							
			else:
				dom.append("\t"*(lvl) + "</"+stack.pop()+">")
				while lvl > tab_count:
					lvl = len(stack)-1					
					dom.append("\t"*(lvl) + "</"+stack.pop()+">")
				dom.append("\t"*tab_count + "<"+line[tab_count:-1]+">")
				stack.append(line[tab_count:-1])
			lvl = tab_count

		while stack:
			dom.append("\t"*(len(stack)-1) + "</"+stack.pop()+">")	

		return dom

	@classmethod
	def open_file(cls, file_to_html):
		with open(file_to_html, 'w') as html_file:
			dom = cls.build_html(f)
			for line in dom:
				html_file.write(line+"\n")
				print line


HtmlGenerator.open_file("html.txt")

# print class_with_staticmethod
# print class_with_classmethod
# print class_with_property.cls_name
