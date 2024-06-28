import random

num_rolls = 1000
rolls = [random.randint(1,6) for _ in range(num_rolls)]

count_6 = 0
count_1 = 0
count_two_6s = 0

for i in range(num_rolls):
    if rolls[i] == 6:
        count_6 += 1
    if rolls[i] == 1:
        count_1 += 1
    if i < num_rolls - 1 and rolls[i] == 6 and rolls[i+1] == 6:
        count_two_6s += 1

print('number of times rolled a 6:', count_6)
print('number of times rolled a 1:', count_1)
print('the number of times rolled two 6s in a row:', count_two_6s)