# Program to find duplicates from a given list
list_1 = [1, 2, 3, "Apple", "Orange"]
list_2 = [4, 5, 6, "Apple", "Blueberry"]
list_3 = [2, 5, 7, "Mango", "Grapes"]
combined_list = list_1 + list_2 + list_3
seen = set()
duplicates = []
for item in combined_list:
    if item in seen:
        if item not in duplicates:
            duplicates.append(item)
    else:
        seen.add(item)
print("Duplicates from the given list:", duplicates)

