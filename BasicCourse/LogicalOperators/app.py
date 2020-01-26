has_high_income = True
has_good_credit = False

# and operator
if has_high_income and has_good_credit:
    print('Eligible for loan')

# or operator
if has_high_income or has_good_credit:
    print('Eligible for loan')

# not operator
has_good_credit = True
has_criminal_record = True

if has_good_credit and not has_criminal_record:
    print('Eligible for loan')
