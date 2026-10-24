# Level 1
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
import functools

# 1:
question1 = """ 
map, filter and reduce take the same parameters, f(function, iterable), but differ in their 
actions and output. 

map: 
- action: iterates through the iterable and modifies each item via the function it calls.
- output: a 'map object'. like the ingredients for a new iterable, same length as original, 
containing each original item's modified version.  

filter: 
- action: calls a boolean function and tests each item in the iterable against the condition.
in this way the condition serves as filtering criteria.
- output: return a list of only items that pass the condition

reduce: 
- action: applies the called function to combine each item in the iterable
- output: a single value
"""

# 2
question2 = """  differences as follows 

higher order function: uses an existing function as an argument, or returns a function

closure: nested function that can access outer variables

decorator: adds functionality to existing object. adds capabilities without changing the 
underlying code
"""

# 3 inserting examples

# using map to convert a list of str into int
numbers_str = ['1', '2', '3', '4', '5']  # iterable
numbers_int = map(int, numbers_str)
print(list(numbers_int))    # [1, 2, 3, 4, 5]

# using filter for even numbers in a list
numbers_again = [1, 2, 3, 4, 5] 

def is_even(num):
    if num % 2 == 0:
        return True
    return False

even_numbers = filter(is_even, numbers_again)
print(list(even_numbers))

# using reduce given numbers str

def add_two_nums(x, y):
    return int(x) + int(y)

total = functools.reduce(add_two_nums, numbers_str)
print(total)    # 15

# 4
for country in countries:
    print(country)

# 5
for name in names: 
    print(name)

# 6
for number in numbers: 
    print(number)