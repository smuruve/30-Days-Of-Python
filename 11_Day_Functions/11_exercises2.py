# Level 2 Exercises
# 1
def evens_and_odds(pos_integer):
    evens = []
    odds = []

    for number in range(pos_integer + 1):
        if number % 2 == 0:
            evens.append(number)
        else:
            odds.append(number)

    print(f"The number of evens is {len(evens)}")
    print(f"The number of odds is {len(odds)}")

evens_and_odds(100) # check
evens_and_odds(99) # check

# 2
def factorial(number): 
    total = 1
    for number in range(1, number + 1): 
        total = total * number

    return total

factorial(5) # check it's 120
factorial(0) # check it's 1

# 3
def is_empty(value): 
    if value: 
        print("This function isn't empty")
    else: 
        print("This function is empty")
    return value

is_empty([]) # empty
is_empty(3) # not empty

# 4
numbers = [1, 2, 3, 4, 5, 6, 7]
numbers2 = [8, 12, 12, 14, 18, 15, 19, 8] # suspecting I'll need to test an even number list for median
numbers3 = [1, 1, 1, 2, 3, 4, 5, 5, 6, 7]

def calculate_mean(numbers):
    total = 0
    for number in numbers:
        total = total + number
    return total / len(numbers)

def calculate_median(numbers):
    numbers.sort()
    if len(numbers) % 2 == 0:
        right_middle = len(numbers) // 2
        left_middle = right_middle - 1
        list_median = (numbers[left_middle] + numbers[right_middle]) / 2

    elif len(numbers) % 2 == 1: 
        middle = len(numbers) // 2
        list_median = numbers[middle]

    return list_median

def calculate_mode(numbers):
    counts = {}
    for number in numbers:
        if number in counts: 
            counts[number] = counts[number] + 1
        else:
            counts[number] = 1

    mode_location = max(counts.values())
    if mode_location == 1: 
        return "no mode"

    for key in counts:
        if counts[key] == mode_location:
            mode = key

    return mode

def calculate_range(numbers):
    numbers.sort()
    range = numbers[-1] - numbers[0]

    return range

def calculate_variance(numbers):
    mean = calculate_mean(numbers)
    deviations = []
    for number in numbers:
        squared_deviation = (mean - number) ** 2
        deviations.append(squared_deviation)
    variance = sum(deviations) / len(numbers)
    return variance

def calculate_std(numbers): 
    listvariance = calculate_variance(numbers)
    std = listvariance ** 0.5
    return std

# some checks
print(calculate_mean(numbers))

print(calculate_median(numbers))
print(calculate_median(numbers2))

print(calculate_mode(numbers))
print(calculate_mode(numbers2))
print(calculate_mode(numbers3))

print(calculate_range(numbers))
print(calculate_range(numbers2))

print(calculate_variance(numbers2))
print(calculate_std(numbers2))

# 4
def greet(name = "Guest"): # default value
    greeting = print(f"Hello, {name}!")
    return greeting

greet()
greet("Sofia")

# 5
def show_args(**args):
    message = "Received: "
    for key, value in args.items():
        message = message + f"{key}: {value}, "
    return message

print(show_args())
print(show_args(name = "Sofia", age = 20, city = "Toronto"))
print(show_args(colour = "Red", language = "Français"))