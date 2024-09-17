#!/usr/bin/python3

import sys 
def print_to_stderr(*a): 
	print(*a, file = sys.stderr) 
print_to_stderr("Hello World")
