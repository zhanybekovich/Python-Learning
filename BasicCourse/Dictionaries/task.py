# My solution
numbers = {
    '0': 'Zero',
    '1': 'One',
    '2': 'Two',
    '3': 'Three',
    '4': 'Four',
    '5': 'Five',
    '6': 'Six',
    '7': 'Seven',
    '8': 'Eight',
    '9': 'Nine'
}

phone_number = input('Phone: ')

for number in phone_number:
    print(numbers[number], end=' ')

print('\n===========')
# Author's solution
phone = input('Phone: ')
output = ''
digit_mapping = {
    '0': 'Zero',
    '1': 'One',
    '2': 'Two',
    '3': 'Three',
    '4': 'Four',
    '5': 'Five',
    '6': 'Six',
    '7': 'Seven',
    '8': 'Eight',
    '9': 'Nine'
}
for ch in phone:
    output += digit_mapping.get(ch, '!') + ' '
print(output)

