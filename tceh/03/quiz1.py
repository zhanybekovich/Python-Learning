import random

num = random.randint(1, 3)
print(num)

def random_error(num):
    if num == 1:
        raise ValueError('V error!')
    elif num == 2:
        raise TypeError('T error!')
    else:
        raise RuntimeError('R error!')

random_error(num)

