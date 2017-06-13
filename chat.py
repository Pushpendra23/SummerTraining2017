#!/usr/bin/python

import os
p='''Press  1 to start chat
Press  2 to join chat'''
print p
a=raw_input()
if a=='1' :
	os.system('nc -l 1234')
elif a=='2' :
	print 'Please enter the ip with you want to communicate'
	b=raw_input()
	os.system('nc '+b+' 1234')

