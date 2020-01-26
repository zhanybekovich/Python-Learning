# My solution
credit_good = False
price = 1000000

if credit_good:
    payment = price * 0.1
    print(f'Your payment is {payment}')
else:
    payment = price * 0.2
    print(f'Your payment is {payment}')

# Author solution
price = 1000000
has_good_credit = True

if has_good_credit:
    down_payment = 0.1 * price
else:
    down_payment = 0.2 * price
print(f'Down payment: ${down_payment}')