#!/usr/bin/python
import string
import os
print "Enter any number to add"
a=raw_input()
sum=0
for i in a:
	if i in string.digits:
		sum=sum+int(i)
	elif i in string.ascii_uppercase or i in string.ascii_lowercase:
		print i+" is an alphabet not a number hence cannot be added"
	else :
		print i+" is not a number"

print "the addition is "
print sum
raw_input()
		
	
