# -*- coding: utf-8 -*-
"""
Exercise #3

Write a program that accepts a comma separated sequence of words as input
and prints the words in a comma-separated sequence after sorting them
alphabetically.

Suppose the following input is supplied to the program:
without,hello,bag,world

Then, the output should be:
bag,hello,without,world

Hint:
String join() method
"""


# your name and email address here
Francis = 'francislouie <francis@bywave.com.au>'


if Francis == '__main__':
    # your code here
	x = raw_input()
	y = x.replace(" ", "")
	z = y.split(",")
	z.sort()
	n = ",".join(z)
	print(n)