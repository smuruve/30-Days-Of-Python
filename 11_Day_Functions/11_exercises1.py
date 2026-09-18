# Level 1 Exercises
# 1
def add_two_numbers(num1, num2): 
    total = num1 + num2
    return total

output1 = add_two_numbers(1, 2)
print(output1)

output2 = add_two_numbers(3, 4)
print(output2) # check it works with different inputs

# 2
def area_of_circle(radius):
    area = 3.14 * radius * radius
    return area

area = area_of_circle(4)
print(area)

def interactive_area(): 
    radius = float(input("Enter radius:"))
    area = 3.14 * radius * radius
    return area

interactive_area() # another way user can provide radius

# 3
def add_all_nums(*nums): 
    total = 0
    for num in nums: 
        total = total + num
    return total

print(add_all_nums(5, 6, 9, 111)) # check

# 4 
def convert_celsius_to_fahrenheit(celsius): 
    fahrenheit = (celsius * (9 / 5)) + 32
    return fahrenheit

convert_celsius_to_fahrenheit(30) # check

# experiment with user facing version
def convert_celsius_to_fahrenheit_user(): 
    celsius = float(input("Enter celsius: "))
    fahrenheit = (celsius * (9 / 5)) + 32
    print(f"{celsius} celsius is equivalent to {fahrenheit} degrees fahrenheit")

convert_celsius_to_fahrenheit_user()

# 5
# user facing more intuitive for some reason
# note to self the result is printed, not returned
def check_season_foruser(): 
    month = input("Enter the month: ").strip().lower()

    autumn = ["september", "october", "november"]
    winter = ["december", "january", "february"]
    spring = ["march", "april", "may"]
    summer = ["june", "july", "august"]

    if month in autumn: 
        print("That month is in autumn.")
    elif month in winter:
        print("That month is in winter.")
    elif month in spring:
        print("That month is in spring.")
    elif month in summer:
        print("That month is in summer.")
    else: 
        print("please enter a month")

check_season_foruser()

# try with just parameters
def check_season(month): 
    month = month.strip().lower()
    autumn = ["september", "october", "november"]
    winter = ["december", "january", "february"]
    spring = ["march", "april", "may"]
    summer = ["june", "july", "august"]

    if month in autumn: 
        return "Autumn"
    elif month in winter: 
        return "Winter"
    elif month in spring:
        return "Spring"
    elif month in summer: 
        return "Summer"

print(check_season("oCtober"))
print(check_season("July "))
print(check_season("DECEMBER"))
print(check_season("april"))

# 6
def calculate_slope(x1, y1, x2, y2): 
    slope = (y2 - y1) / (x2 - x1)
    return slope

# 7
def solve_quadratic_eqn(a, b, c): 
    x1 = (-b + (((b **2) - 4 * a * c) ** 0.5)) / (2 * a)
    x2 = (-b - ((b ** 2) - 4 * a * c) ** 0.5) / (2 * a)
    return x1, x2

solve_quadratic_eqn(1, -5, 6) # check: solution set is x = 2 and x = 3

# 8
def print_list(list): 
    for word in list: 
        print(word)

peakveg = ["carrots", "cabbage", "spinach", "tomato", "cauliflower", "fennel"]

print_list(peakveg) # check

# 9
def reverse_list(array): 
    reversed_items = [] 
    for index in range(len(array) -1, -1, -1): 
        reversed_items.append(array[index])
    return reversed_items

reverse_list(["carrots", "cabbage", "spinach", "tomato", "cauliflower", "fennel"]) # check

# 10
def capitalize_list_items(list): 
    capitalized_list = []
    for word in list: 
        capitalized_list.append(word.title())
    return capitalized_list

capitalize_list_items(peakveg) # check

# 11 
def add_item(list, *new_items):
    for item in new_items: 
        list.append(item)
    return list

add_item(peakveg, "pepper") # check
add_item(peakveg, "jicama", "beets") # check multiple arguments

# 12
def remove_item(list, *remove_items): 
    for item in remove_items:
        list.remove(item)
    return list

remove_item(peakveg, "pepper") # check
remove_item(peakveg, "jicama", "beets") # check multiple arguments

# 13
def sum_of_numbers(number): 
    total = 0
    for number in range(number + 1): 
        total = total + number 
    return total

sum_of_numbers(5) # check it's 15
sum_of_numbers(10) # check it's 55
sum_of_numbers(100) # check it's 5050

# 14
def sum_of_odd(number): 
    total = 0
    if number % 2 == 1: 
        for number in range(number + 1):
            if number % 2 == 1: 
                total = total + number
                
    else: 
        for number in range(number): 
            if number % 2 == 1:
                total = total + number

    return total 

sum_of_odd(100) # should be 2500
sum_of_odd(5) # should be 9


# 15
def sum_of_even(number): 
    total = 0
    for number in range(number + 1): 
        if number % 2 == 0: 
            total = total + number
    return total # should be 2550

sum_of_even(100) # should be 2550
sum_of_even (5) # should be 6