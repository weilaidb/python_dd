#!/usr/bin/python
#Filename:class__init__.py
class Person:
	def __init__(self,name):
		self.name = name
	def sayHi(self):
		print 'Hello,my name is', self.name

p = Person('Weilaidb')
p.sayHi()
