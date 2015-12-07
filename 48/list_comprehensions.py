#!/usr/bin/python
#Filename:list_comprehensions.py
#列表推导 List comprehensions


import os
import sys



numbers = range(10)
numbers
print numbers

size = len(numbers)
print 'len(numbers):',  size

events = []
i = 0

while i < size:
    if i % 2 == 0:
        events.append(i)
    i += 1
    
events
print events




##
print [i for i in range(10) if i % 2 ==0 ]


##
i = 0
seq = ["one", "two", "three"]
for element in seq:
    seq[i] = '%d:%s' % (i,seq[i])
    i += 1

print seq

##
seq = ["one", "two", "three"]
for i,element in enumerate(seq):
    seq[i] = '%d:%s' % (i, seq[i])
    
print seq

##
def _treatement(pos,element):
    return '%d:%s' % (pos,element)

seq = ["one", "two", "three"]
print [_treatement(i, el) for i,el in enumerate(seq)]
    



