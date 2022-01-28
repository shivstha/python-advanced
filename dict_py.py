from ast import Or
from platform import java_ver


my_dict = { }

# or my_dict = dict()

# checking object type
print(type(my_dict))

# adding first pair
my_dict['C'] = "Dennis Ritchie "

# adding second pair
my_dict['C++'] = "Bjarne Stroustrup"

# adding third pair
my_dict['Python'] = "Guido van Rossum"

# adding fourth pair
my_dict['Java'] = "James Gosling"

print(my_dict)

# accessing values

# get the developer of Python
print(my_dict["Python"])

# get the developer of Java
print(my_dict["Java"])

# modify Python value
# change value to Van Rossum
my_dict['Python'] = "Van Rossum"

print(my_dict["Python"])

# looping through items
for key, value in my_dict.items():
    print(f'{key} was developed by {value}')

# looping through keys
print("All the programming languages")
for key in my_dict.keys():
    print(key)

# OR
for key in my_dict:
    print(key)

# looping through keys
print("All the developers")
for value in my_dict.values():
    print(value)


# removing key:value pair
# remove Java as key
del my_dict["Java"]

print(my_dict)

# to clear the dictionary
my_dict.clear()

print(my_dict)

# to delete the dictionary object
del my_dict

print(my_dict)