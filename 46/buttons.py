#!/usr/bin/python
#Filename:buttons.py

import gtk

class PyApp(gtk.Window):
	def __init__(self):
		super(PyApp, self).__init__()
		
		self.set_title("Button Test")
		self.set_size_request(250,150)
		self.set_position(gtk.WIN_POS_CENTER)
		
		btn1 = gtk.Button("Button1")
		btn1.set_sensitive(False)
		btn2 = gtk.Button("Button2")
		btn3 = gtk.Button(stock=gtk.STOCK_CLOSE)
		btn4 = gtk.Button("Button4")
		btn4.set_size_request(80, 40)
		
		fixed = gtk.Fixed()
		
		fixed.put(btn1, 20,  30)
		fixed.put(btn2, 100, 30)
		fixed.put(btn3, 20,  80)
		fixed.put(btn4, 100, 80)
		
		self.connect("destroy", gtk.main_quit)
		
		self.add(fixed)
		self.show_all()
		

PyApp()
gtk.main()