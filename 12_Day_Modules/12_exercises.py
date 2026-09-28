# Level 1
# 1
import random
import string

def random_user_id():
    length = 6
    result = "" # assign it as an empty string
    choices = (string.ascii_letters + string.digits)

    for loopcountingvariable in range(length):
        result = result + random.choice(choices)

    return result

print(random_user_id())

# 2 
def user_id_gen_by_user():
    characters = int(input("Enter how many characters would you like in each ID: "))

    num_ids = int(input("Enter the number of IDs you would like to generate: "))

    choices = (string.ascii_letters + string.digits)

    for _ in range(num_ids): 
        result = "" 

        for _ in range(characters):
            result = result + random.choice(choices)

        print(result)

user_id_gen_by_user()

# 3
def rgb_color_gen():
    result = []
    for _ in range(3): 
        result.append(random.randint(0, 255))

    return f"rgb({result[0]}, {result[1]}, {result[2]})"

print(rgb_color_gen())

# Level 2
# 1
def list_of_hexa_colors(desired_number): 
    hexa_list = []
    for _ in range(desired_number): 
        hexa_chars = "abcdef" + string.digits

        hexa = []
        for _ in range(6): 
            hexa.append(random.choice(hexa_chars))
        
        unifiedhexa = "#" + "".join(hexa)
        hexa_list.append(unifiedhexa)

    return hexa_list

print(list_of_hexa_colors(5))

# 2
def list_of_rgb_colors(desired_number): 
    rgb_list = []
    for _ in range(desired_number): 
        rgb_list.append(rgb_color_gen())

    return rgb_list

print(list_of_rgb_colors(2))

# 3
def generate_colors(color_type: str, desired_number: int): 
    message = "Please indicate which type of colour: hexa or rgb?"
    
    if color_type.lower() == "hexa":
        return list_of_hexa_colors(desired_number)
    elif color_type.lower() == "rgb":
        return list_of_rgb_colors(desired_number)
    else: 
        return message

print(generate_colors("Hexa", 6))
print(generate_colors("rgb", 3))

# Level 3
# 1
def shuffle_list(my_list: list):
    return random.sample(my_list, k = len(my_list))

fruits = ["banana", "kiwi", "strawberry", "orange", "grape"]
print(shuffle_list(fruits))

# 2
def array_of_seven():
    return random.sample(range(10), 7)

print(array_of_seven())