# -*- coding: utf-8 -*-
# python 2.7.9

x=5
def factorial(i):
	if i == 0:
		return 1
	else:
		return i * factorial(i - 1)
print factorial(x)