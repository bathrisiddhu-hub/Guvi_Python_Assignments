# in the given list separate even and odd numbers into different lists
python_list = [10, 501, 22, 37, 100, 999, 87, 351]
even_list = []
odd_list = []
for num in python_list:
    if num % 2 == 0:
        even_list.append(num)
    else:
        odd_list.append(num)
print(f"Even number list: {even_list}")
print(f"Odd number list: {odd_list}")