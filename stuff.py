# output = 5/2
# print(output)

# output_list = ['cool', 5, 5.1, True]
# print(output_list)

# output_list.append('new')
# print(output_list)

# output_tuple = {
#     'something',
#     4,
#     8.1,
#     True
# }

# print(output_tuple)

# # Lists are mutable, tuples are not

# # Search PEP8 for best practices

# bool_variable = True

# if bool_variable:
#     print("It's true")
# else:
#     print("It's false")

# sample_dictionary = {
#     3: 'value',
#     'number': 5,
#     'list': [
#         1,
#         2.3,
#         'string'
#     ],
#     {
#         'key': 'new value'
#     }: {
#         'another key': 'new, new value'
#     }
# }

# dictionaries require a {}, not a []
# dictionaries are mutable

# sample_dictionary['address'] = '1234 Party Ln'
# print(sample_dictionary)

# Problem w/dictionaries is when you add something, it may not be in the same order as when you add a new value, which is different from a tuple. It's a "hashable index"

# print(sample_dictionary[3])

# The dictionary above is just an example of how you can have objects w/in objects - dictionaries w/in dictionaries, etc.

# Dictionaries are like objects in JS

# dictionary_people = {
#     'individual': {
#         'maria': {
#             'age': 50,
#             'height': 60
#         }
#     }
# }

# name_ = 'Billy'
# string_1 = 'Hi, my name is ' + name_ + '. Nice to meet you.'
# string_2 = 'Hi, my name is {}. Nice to meet you.'.format(name_)
# string_3 = f'Hi, my name is {name_}. Nice to meet you.'

# print(f'{string_1}\n{string_2}\n{string_3}')

# def multiply_these_numbers(first_number, second_number):
#     return first_number * second_number

# print(multiply_these_numbers(5, 10))

# first_number = 3
# second_number = 20

# def multiply_these_numbers():
#     global first_number
#     global second_number
#     first_number = 2
#     second_number = 5
#     print(f'Inside the function: {first_number}, {second_number}')
#     return first_number * second_number

# print(f'Outside the function: {first_number}, {second_number}')
# print(multiply_these_numbers())

# You can use an asterisk to unpack something, like a tuple: *multiply_tuple
def unpack_tuple():
    nom_1 = 2
    nom_2 = 5
    return nom_1, nom_2

print(*unpack_tuple())

# You can make a variable private - only accessible w/in the scope where it is used - when you put an underline in front of the variable: Example - _variable

# set: Set is similar to a dictionary but the keys can't be reordered
example_set = {'key1', 'key2', 'key3'}
print(example_set)
del example_set
print(example_set)

