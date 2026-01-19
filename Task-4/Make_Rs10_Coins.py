# Find all the ways to make Rs 10 using Rs 1, Rs 2 , Rs 5 and Rs 10 coins without using functions.
coin_list = [1, 2, 5, 10]
target = 10
number_of_ways = 0

for c1 in range(target // coin_list[0] + 1):
    for c2 in range(target // coin_list[1] + 1):
        for c5 in range(target // coin_list[2] + 1):
            for c10 in range(target // coin_list[3] + 1):
                total = (c1 * coin_list[0]) + (c2 * coin_list[1]) + (c5 * coin_list[2]) + (c10 * coin_list[3])
                if total == target:
                    number_of_ways += 1
                    print(f"way {number_of_ways}: {c1}x1, {c2}x2, {c5}x5, {c10}x10")
print(f"Total number of ways to make Rs10: {number_of_ways}")
















