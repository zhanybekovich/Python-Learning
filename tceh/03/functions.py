def first(x):
    return x + 10

print(first(10))


def second(x, z):
    return x + z


print(second(10, 30))

def zero_params():
    return 'No params'


print(zero_params())

def return_none(x):
    print('Params was', x)

test = return_none(6)
return_none(7)

def sum_numbers(n1, n2, n3):
    print(n1, n2, n3, 'summing...')
    return n1 + n2 + n3

total = sum_numbers(7, 0.3, 0.3)
print(total)

def my_function(var1, var2, var3):
    print("No way I'm using this: {}, {}, {}".format(var1, var2, var3))

new_call = my_function(1, 2, 3)
print(new_call)