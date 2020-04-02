# Pure Functions 
# We cannot change anything in the internal state and the function must
# always give the same output for the same input

def impure_doubling(num_list):
    for i, n in enumerate(num_list):
        num_list[i] = 2 * n
    return num_list

def pure_doubling(num_list):
    new_num_list = []
    for n in num_list:
        new_num_list.append(n * 2)
    return new_num_list

# a = [1, 3, 5, 10]
# b = impure_doubling(a)
# print(b)
# b = impure_doubling(a)
# print(b)

# Immutability
# Favour immutable objects where possible so behaviour is not accidentally
# changed elsewhere


# mutable = ['Notorious D.O.G', 'Mary Puppins', 'Whelp the Aged', 'Dogtor Who']
# immutable = ('Dumbledog', 'Sue Barker', 'Woofus Hound', 'Wolf Harris')

# mutable[1] = 'Shallow Howl'
# immutable[1] = 'Shallow Howl'

# Functions are First Class Objects
# Remember that functions can be passed to other functions in Python. 
# Functions can also return functions.

# def pure_doubling(num_list):
#     new_num_list = []
#     for n in num_list:
#         new_num_list.append(n * 2)
#     return new_num_list

# def pure_tripling(num_list):
#     new_num_list = []
#     for n in num_list:
#         new_num_list.append(n * 3)
#     return new_num_list 

a = [1, 3, 5, 10]
# b = pure_doubling(a)
# print(b)
# c = pure_tripling(a)
# print(c)

# def pure_multiplication(scalar):
#     def scalar_multiply(num_list):
#         new_num_list = []
#         for n in num_list:
#             new_num_list.append(n * scalar)
#         return new_num_list   
#     return scalar_multiply      

# a = [1, 3, 5, 10]
# pure_quadrupling = pure_multiplication(4)
# d = pure_quadrupling(a)
# print(d)





