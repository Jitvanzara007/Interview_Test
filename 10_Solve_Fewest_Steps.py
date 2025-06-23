'''
using simple logic fist sorted letters and digits then join them together in sorted order'''

def sort_string(a):
    letters = sorted([ch for ch in a if ch.isalpha()])
    digits = sorted([ch for ch in a if ch.isdigit()])
    return ''.join(letters + digits)

input = "B4A1D3"
print(sort_string(input)) 