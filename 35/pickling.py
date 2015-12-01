#!/usr/bin/python
#Filename:pickling.py
import cPickle as p
#import cPickle as p
shoplistfile = 'shoplist.data'
#the name of the file where we will store the object
shoplist = ['apple','mango','carrot','test']
#Write to the file
f = file(shoplistfile,'w')
p.dump(shoplist,f)
f.close()

del shoplist

f = file(shoplistfile)
storedlist = p.load(f)
print storedlist
