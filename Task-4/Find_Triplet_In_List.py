# Find a triplet in a list that sums to a given value
list_number = [10, 20, 30, 9]
value = 59
n = len(list_number)
for i in range(n -2):
    for j in range(i + 1, n -1):
        for k in range(j + 1, n):
            if list_number[i] + list_number[j] + list_number[k] == value:
                print(f"Triplet found: {list_number[i]}, {list_number[j]}, {list_number[k]}")
                break


