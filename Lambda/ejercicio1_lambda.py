# Example: Use lambda function with built-in Python method reduce.
from functools import reduce

numbers = [5, -6, 2, 7]
total = reduce(lambda x, y: x + y, numbers)
print(f'The sum of the numbers is {total}.')

#otro ejemplo
# Example: Use lambda function with built-in Python method zip.
list1 = [1, 2, 3]
list2 = [4, 5, 6]

# Using zip and a lambda function to multiply corresponding elements
result = list(map(lambda x: x[0] * x[1], zip(list1, list2)))

print(f'The result of multiplying corresponding elements is {result}.')