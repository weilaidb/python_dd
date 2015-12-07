#!/usr/bin/python
# -*- coding: UTF-8 -*-
#coding=gb2312
#Filename:iterator.py 
##迭代器 Iterators



i = iter('abc')
print i.next()
print i.next()
print i.next()
# print i.next() #error
# print i.next()

print
# print



##
class MyIterator(object):
    def __init__(self, step):
        self.step = step
    
    def next(self):
        """Returns the next element."""
        if self.step == 0:
            raise StopIteration
        self.step -= 1
        return self.step
    
    def __iter__(self):
        """Returns the iterator itself."""
        return self
    
    

for el in MyIterator(4):
    print el
    
#error info
# for el in MyIterator("abcd"):
#     print el
    