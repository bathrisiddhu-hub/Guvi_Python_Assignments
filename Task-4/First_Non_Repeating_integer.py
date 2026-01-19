# Program to find the first non-repeating integer in a list
list_numbers = [1, 2, 3, 2, 1, 4, 5, 4, 6]
non_repeating = {}
for num in list_numbers:
    if num in non_repeating:
        non_repeating[num] += 1
    else:
        non_repeating[num] = 1
for num in list_numbers:
    if non_repeating[num] == 1:
        print("First Non-Repeating element in the given list:", num)
        break






