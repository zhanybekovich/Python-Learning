customer = {
    'name': 'John Smith',
    'age': 30,
    'is_verified': True
}
print(customer['name'])

# if there's no a key in the dict
# it's possible to insert a default value
print(customer.get('birthdate', 'Jan 1 1980'))

# updating values
customer['name'] = 'Jack Smith'
print(customer['name'])

# adding a new key
customer['birth_date'] = 'Jan 2 1981'
print(customer['birth_date'])
