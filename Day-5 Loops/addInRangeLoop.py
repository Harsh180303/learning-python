# sum of all the even number from 1 to 100 including 1 and 100

total = 1
for number in range(2, 101, 2):
    total += number

print(total)