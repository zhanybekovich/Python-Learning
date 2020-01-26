# My solution
numbers = [2, 2, 4, 6, 3, 4, 6, 1]
for number in numbers:
    if numbers.count(number) > 1:
        numbers.remove(number)
print(numbers)

# Author's solution
numbers = [2, 2, 4, 6, 3, 4, 6, 1]
uniques = []

for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)