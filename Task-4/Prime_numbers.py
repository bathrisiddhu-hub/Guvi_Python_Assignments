# Write a Python program to find all prime numbers in a given list of numbers.
python_list = [10, 501, 22, 37, 100, 999, 87, 351]
prime_number_list = []
for num in python_list:
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            prime_number_list.append(num)
print("Prime numbers in the list:", prime_number_list)

