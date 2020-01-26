# My solution
weight = int(input('Weight: '))
lbs_or_kg = input('(L)bs or (K)g: ')

if lbs_or_kg.lower() == 'l':
    weight_kg = weight * 0.45
    print(f'You are {weight_kg} kilos')
else:
    weight_lbs = weight / 0.45
    print(f'You are {weight_lbs} pounds')

# Author's solution
# weight = int(input('Weight: '))
# unit = input('(L)bs or (K)g: ')
#
# if unit.upper() == 'L':
#     converted = weight * 0.45
#     print(f'You are {converted} kilos')
# else:
#     converted = weight / 0.45
#     print(f'You are {converted} pounds')
