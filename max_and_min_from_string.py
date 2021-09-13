# max_and_min_from_string.py

string = '-1 2 3 9 -5 4 8'

def max_and_min_from_string(string):
    lst = string.split()
    new_list = []
    for item in lst:
        new_list.append(int(item))
    return (f"{max(new_list)} {min(new_list)}")

print(f'{max_and_min_from_string(string)=}')

# Here is a better solution that uses a Python construct called comprehension.
# This code was written by xavierguihot, gontzalm, and kwürm who are competitors
# on the CodeWars website.

def high_and_low(numbers):
    numbers = [int(c) for c in numbers.split(' ')]
    return f"{max(numbers)} {min(numbers)}"

print(f'{high_and_low(string)=}')