# Find the minimum element in a rated  and sorted list without using functions.
sorted_list = [4, 5, 6, 7, 0, 1, 2]
min_element = sorted_list[0]
for num in sorted_list:
    if num < min_element:
        min_element = num
print("Minimum element in the rotated and sorted list:", min_element)
