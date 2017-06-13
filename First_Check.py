#!/usr/bin/python
import  string
print "enter first number to add"
a=raw_input()
if a[0] in string.digits:
	print "enter second number to add"
	b=raw_input()
	if b[0] in string.digits:
		c=int(a)+int(b)
		print "result:"
		print c
	else:
		print "not valid"
elif a[0] in string.ascii_lowercase or a[0] in string.ascii_uppercase:
	print "you entered a alphabet"
else:
	print "you entered a special character"
raw_input()

