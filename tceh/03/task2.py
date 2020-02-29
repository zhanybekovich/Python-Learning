l = [1, 'abra', 9, 7, 'true']

try:
    user_input = int(input('Enter your choice: '))
    print(l[user_input])
except IndexError:
    print('There is no such index!')
except ValueError:
    print('Oops it is not a number!')