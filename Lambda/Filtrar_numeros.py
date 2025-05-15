# Use filter with lambda function
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
evens = filter(lambda x: x % 2 == 0, numbers)
print(list(evens))  # print the list of the filter object to see the result

#ejemplo 2
# Use map with lambda function
fruits = ['apple', 'banana', 'cherry']
lengths = list(map(lambda x: len(x), fruits))
print(lengths)

# Sort a list of tuples by the second element
data = [(1, 3), (2, 1), (4, 2)]
sorted_data = sorted(data, key=lambda x: x[1])
print(sorted_data)