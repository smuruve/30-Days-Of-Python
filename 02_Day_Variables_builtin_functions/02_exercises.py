# Day 2: 30 Days of Python Programming. Level 1
first_name = "Sofia"
last_name = "Muruve"
full_name = "Sofia Muruve"
country = "Canada"
city = "Township of Muskoka Lakes"
age = 20
year = 2026
is_married = False
is_true = True
is_light_on = True
x, y, z = "red", "yellow", "green"

# Moving on to Level 2. 
print(len(first_name))
print(len(last_name))
print(len(first_name) > len(last_name))
num_one, num_two = 5, 4

total = (num_one + num_two)
diff = (num_one - num_two)
product = (num_one * num_two)
division = (num_one / num_two)
remainder = (num_two % num_one)
exp = (num_one ** num_two)
floor_division = (num_one // num_two)

radius = 30
area_of_circle = 3.14 * (radius ** 2)
circumference_of_circle = 2 * 3.14 * radius

#taking radius as user input: 
radius = float(input("Enter the radius: "))

area_of_circle = 3.14 * (radius ** 2)
circumference_of_circle = 2 * 3.14 * radius

# input for gathering and storing info from user
user_firstname = input("Enter your first name: ")
user_lastname = input("Enter your last name: ")
user_country = input("Enter your country: ")
user_age = input("Enter your age: ")

# printing variables
print(total)
print(diff)
print(product)
print(division)
print(remainder)
print(exp)
print(area_of_circle)
print(circumference_of_circle)