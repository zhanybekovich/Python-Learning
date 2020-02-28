# default arg
def with_default(name='Mir'):
    print('Hello', name)

with_default('Pete')
with_default()

# positional and default args
def with_many(pos, default_arg='some'):
    print(pos, default_arg)

with_many(9, 'm')
with_many(9)

# any number of args
def sum_all(*numbers):
    s = 0
    for number in numbers:
        s = s + number
    
    return s

print(sum_all(1, 8, 3))

# any number of keyword args
def any_keywords(**kwargs):
    print(kwargs, type(kwargs))

any_keywords(k=1, some=2, wo=3)

