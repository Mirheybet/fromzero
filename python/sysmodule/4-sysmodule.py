#!/usr/bin/python3



import sys

n = len(sys.argv)
print("Total arguments( with program name ) passed:", n)

print("\nName of Python script:", sys.argv[0])

print("\nArguments passed:", end = " ")
for i in range(1, n):
    print(sys.argv[i], end = " ")
    
# Addition of numbers
Sum = 0
# Using argparse module
for i in range(1, n):
    Sum += int(sys.argv[i])
    
print("\n\nResult:", Sum)

