numbers = [5, 2, 1, 7, 4]
# adding new item
numbers.append(20)
print(numbers)

# inserting new item
numbers.insert(0, 10)
print(numbers)

# removing items
numbers.remove(5)
print(numbers)

# removing all items
numbers.clear()
print(numbers)

# removing the last item
numbers = [5, 2, 1, 7, 4]
numbers.pop()
print(numbers)

# checking the existence
print(numbers.index(5))
print(50 in numbers)
print(numbers.count(5))

# sorting
# ascending order
numbers.sort()
print(numbers)
#descending order
numbers.reverse()
print(numbers)

# copying
numbers2 = numbers.copy()
numbers2.append(100)
print(numbers2)

