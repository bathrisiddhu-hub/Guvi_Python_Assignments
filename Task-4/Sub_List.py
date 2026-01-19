# find the sub-list with sum equal to zero
# beginner level code
list_numbers = [4, 2, -3, 1, 6]
sub_list = []
found = False
for i in range(len(list_numbers)):
    current_sum = 0
    for j in range(i, len(list_numbers)):
        current_sum += list_numbers[j]
        if current_sum == 0:
            sub_list = list_numbers[i:j+1]
            found = True
            break
    if found:
        break
if sub_list:
    print("Sub-list with sum equal to zero:", sub_list)
else:
    print("No sub-list with sum equal to zero found.")

