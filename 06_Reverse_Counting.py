'''
#Write a Python program that prints numbers from 1000 down to 1 without using any loops (for,
 while) or the any built-in functions like range().'''

'''
By default, Python allows only about 1000 recursive calls.
sys.setrecursionlimit(1100) increases the limit to 1100.'''
import sys
sys.setrecursionlimit(1100)

def reverse_count(n):
    if n < 1:
        return
    print(n)
    reverse_count(n - 1)
print("Counting down from 1000 to 1:")
reverse_count(1000)