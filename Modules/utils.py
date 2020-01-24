# My solution
# def find_max(numbers, max=''):
#     max = numbers[0]
#     for number in numbers:
#         if number > max:
#             max = number
#     return max


# Author's solution
def find_max(numbers):
    maximum = numbers[0]
    for number in numbers:
        if number > maximum:
            maximum = number
    return maximum
