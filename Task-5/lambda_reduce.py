# use reduce function and lambda expression to calculate the product of all numbers in a list.
from functools import reduce
numbers_list = [3, 5, 10, 2, 7, 8]
product = reduce(lambda x, y: x * y, numbers_list)
print("Product of all numbers in the list:", product)

