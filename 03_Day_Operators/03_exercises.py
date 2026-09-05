# assigning int, float, complex values to variables
my_age = 20 
height_cm = 160.02
complex = 3 + 3j

# 4: calculating area
print("Want to know the area of a triangle?")
b = float(input("Enter the triangle's base: "))
h = float(input("Enter the triangle's height: "))

area = 0.5 * b * h

print ("The area of the triangle is", area)

# 5 perimeter
print("Next up. Want to know the perimeter of a triangle?")
side_a = float(input("Enter the length of side a: "))
side_b = float(input("Enter the length of side b: "))
side_c = float(input("Enter the length of side c: "))

perimeter = side_a + side_b + side_c

print("The perimeter of the triangle is", perimeter)

# 6 rectangle length and width
print("How about the perimeter and area of a rectangle?")
rect_length = float(input("Enter the length: "))
rect_width = float(input("Enter the width: "))

rect_area = rect_length * rect_width
rect_perimeter = 2 * (rect_length + rect_width)

print ("The perimeter of the rectangle is", rect_perimeter)
print ("The area of the rectangle is", rect_area)

# 7 radius, area, circumference
print("Would you like to know the area of a circle?")
radius = float(input("Enter the radius"))
circle_area = 3.14 * radius * radius
circle_circumference = 2 * 3.14 * radius
print("The area is", circle_area)
print("The circumference is", circle_circumference)

# 8 slope of a line, y = 2x - 2
slope1 = 2
x_int = 1
y_int = -2

# 9 equation and euclidean distance
x1 = 2
y1 = 2
x2 = 6
y2 = 10

slope2 = (y2 - y1)/(x2 - x1)
distance = ((x2 - x1) **2 + (y2 - y1) **2) ** 0.5
print("The distance between points (",x1,",",y1,") and (",x2,",",y2,") is", distance)

# 10 compare
print(slope1 == slope2)

# 11
x = -9
y = (x ** 2) + (6 * x) + 9
print(y)

# 12 
print(len("python"))
print(len("dragon"))
len("python") > len("dragon")

# 13
"on" in "dragon" and "on" in "python"

# 14
"jargon" in "I hope this course is not full of jargon"

# 15
"on" not in "dragon" and "on" not in "python"

# 16. learned here about nested functions and working on the inner first. 
str(float(len("python")))
# carries out instructions to first find length of text, then convert to float, then to string.

# 17 use modulus to check if a number is even?
number = float(input("Enter your number"))
number % 2
if number % 2 == 0: 
    print(number, "is even")
else: 
    print(number, "is odd")

# 18 
7 // 3 == int(2.7)

# 19
type("10") == type(10)

# 20 
int(float("9.8")) == 10

# 21
hours = float(input("Enter weekly hours:"))
rate = float(input("Enter pay rate per hour, in dollars:"))
weekly_earning = (hours * rate)
print("Your weekly pay is:", weekly_earning)

# 22
years_alive = float(input("Enter how many years you've lived"))
seconds_alive = years_alive * 365 * 24 * 60 * 60
print("You have lived a total of", seconds_alive, "seconds so far")

# 23
number = 1
print (number, 1, number, number ** 2, number ** 3)
number = 2
print (number, 1, number, number ** 2, number ** 3)
number = 3
print (number, 1, number, number ** 2, number ** 3)
number = 4
print (number, 1, number, number ** 2, number ** 3)
number = 5
print (number, 1, number, number ** 2, number ** 3)