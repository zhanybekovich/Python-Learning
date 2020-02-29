def sum_or_subtr(a, b):
    if a > 0 and b > 0:
        return a + b
    elif a < 0 and b < 0:
        return a - b
    elif a < 0 or b < 0:
        return 0

print(sum_or_subtr(-2, -3))