import random

HANGMAN = (
"""
 ------
 |    |
 |
 |
 |
 |
 |
 |
 |
----------
""",
"""
 ------
 |    |
 |    O
 |
 |
 |
 |
 |
 |
----------
""",
"""
 ------
 |    |
 |    O
 |   -+-
 | 
 |   
 |   
 |   
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-
 |   
 |   
 |   
 |   
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-/
 |   
 |   
 |   
 |   
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-/
 |    |
 |   
 |   
 |   
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-/
 |    |
 |    |
 |   | 
 |   | 
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-/
 |    |
 |    |
 |   | |
 |   | |
 |  
----------
""")

MAX_WRONG = len(HANGMAN) - 1

WORDS = (
    "OVERUSED",
    "CLAM",
    "GUAM",
    "tAFFETA",
    "PYTHON"
)

word = random.choice(WORDS)
so_far = "-" * len(word)
wrong = 0
used = []

print("Добро пожаловать в игру Виселица, Удачи Вам!")
while wrong < MAX_WRONG and so_far != word:
    print(HANGMAN[wrong])
    print("Вы уже предлагали следующие буквы: ", used)
    print("Отгадываемое слово сейчас выглядит так: ", so_far)
    guess = input("Введите букву: ")
    guess.upper()
    while guess in used:
        print("Вы уже предлагали букву", guess)
        guess = input("Введите букву: ")
        guess.upper()
    used.append(guess)

    if guess in word:
        print(f"Да, Буква {guess} есть в слове!")
        new = ""
        for i in range(len(word)):
            if guess == word[i]:
                new += guess
            else:
                new += so_far[i]
        so_far = new
    else:
        print(f"К сожалению, буквы {guess}, нет в слове")
        wrong += 1

if wrong == MAX_WRONG:
    print(HANGMAN[wrong])
    print("Вас повесили!")
else:
    print("Вы отгадали!")
print(f"Было загадано слово {word}")
input("Нажмите Enter, чтобы выйти.")