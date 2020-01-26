# My solution
class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print('Talk')


user = Person('Jack')
user.talk()


# Author's solution
class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f'Hi, I am {self.name}')


john = Person('John Smith')
print(john.name)
john.talk()

bob = Person('Bob Smith')
bob.talk()