# my solution
name = input('Enter your name: ')

if len(name) < 3:
    print('Name must be at least 3 characters')
elif len(name) > 50:
    print('Name can be a maximum of 50 character')
else:
    print('Name looks good!')

# author's solution
# name = 'J'
#
# if len(name) < 3:
#     print('Name must be at least 3 characters')
# elif len(name) > 50:
#     print('Name can be a maximum of 50 character')
# else:
#     print('Name looks good!')