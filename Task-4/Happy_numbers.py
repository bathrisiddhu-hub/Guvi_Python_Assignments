# find out the happy numbers in the given python list:
python_list = [10, 501, 22, 37, 100, 999, 87, 351]
happy_numbers_list = []
for num in python_list:
    seen = set()
    current = num
    while current != 1 and current not in seen:
        seen.add(current)
        current = sum(int(digit) ** 2 for digit in str(current))
        if current == 1:
            happy_numbers_list.append(num)
print("Happy numbers from the list:", happy_numbers_list)


