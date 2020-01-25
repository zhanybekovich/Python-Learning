# My solution
import random

# dice1 = random.randint(1, 6)
# dice2 = random.randint(1, 6)
#
# print(f'({dice1}, {dice2})')

# Author's solution


class Dice:
    def roll(self):
        first = random.randint(1, 6)
        second = random.randint(1, 6)
        return first, second


dice = Dice()
print(dice.roll())