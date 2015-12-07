#!/usr/bin/python
# -*- coding: UTF-8 -*-
#coding=gb2312
#Filename:generator.py 
#生成器 Generators


def fibonacci():
    a, b = 0, 1
    while True:
        yield b  #yield类似于C中的返回 return,即yidld b =>> return b,可以返回多个，如yield a,b,c,是一个无组
        a, b = b, a + b
#         
        

fib = fibonacci()
print fib.next()
print fib.next()
print fib.next()
print fib.next()
print fib.next()
print fib.next()
print fib.next()
print fib.next()
print fib.next()
print fib.next()

print

##
fib = fibonacci()
print [fib.next() for i in range(20)]

print
print
##
poem = '''\
Programming is fun
When the work is done
if you wanna make your work also fun:
        use Python!
'''
f = file('amina.py', 'w') # open for 'w'riting
f.write(poem) # write text to file
f.close() # close the file

##来自标准程序库的tokenize模块将在文本之外生成令牌，并且针对每个处理过的行返回一个迭代器
import tokenize
reader = open('amina.py').next
tokens = tokenize.generate_tokens(reader)
print tokens.next()
print tokens.next()
print tokens.next()
print tokens.next()
print tokens.next()






##
def power(values):
    for value in values:
        print 'powering %s' % value
        yield value


def adder(values):
    for value in values:
        print 'adding to %s' % value
        if value % 2 == 0:
            yield value + 3
        else:
            yield value + 2
  
print
elements = [1,4,7,9,12,19]
res = adder(power(elements))

# print [res.next() for i in range(len(elements))]

print res.next()
 
print res.next()
 
print res.next()
 
print res.next()
 
print res.next()
 
print res.next()



def psychologist():
    print 'Please tell me your problems'
    while True:
        answer = (yield)
        if answer is not None:
            if answer.endswith('?'):
                print ("Don't ask yourself too much questions")
            elif 'good' in answer:
                print "A that's good, go on"
            elif 'bad' in answer:
                print "Don't be so negative"
                
                
#send的工作机制与next一样，但yield将变成能够返回传入的值，可根据客户端的代码来改变其行为
free = psychologist()
free.next()

free.send('I fell bad')

free.send("Why I shouldn't ?")

free.send("ok then i should find what is good for me")


##
def my_generator():
    try:
        yield 'something'
    except ValueError:
        yield 'dealing with the exception'
    finally:
        print "ok let's clean"

print
print
gen = my_generator()
gen.next()

gen.throw(ValueError('mean mean mean'))
gen.close()

# gen.next()

