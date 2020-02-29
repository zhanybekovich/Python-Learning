num = int(input('Enter your number: '))

try:
    if num % 2 == 0:
        raise ValueError("Value Error!!!")
    elif num < 0:
        raise TypeError("T error")
    elif num > 10:
        raise IndexError('Index error')