# Create a new list of squares of even numbers from the given list using list comprehension and using lambda function to check for even numbers.
list_numbers = [1, 2, 3, 6, 7, 10]
square_list = [x**2 for x in list_numbers if (lambda y: y % 2 == 0)(x)]
print("square of even numbers in the give list:", square_list)


