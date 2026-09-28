import mymodule
print(mymodule.generate_full_name("Sofia", "Muruve"))

from mymodule import generate_full_name, sum_two_nums, person, gravity

print(generate_full_name("Sofia", "Muruve"))

mass = 100
weight = mass * gravity
print(weight)

print(person["firstname"])

import os
os.getcwd()
