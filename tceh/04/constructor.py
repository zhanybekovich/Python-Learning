class TestClass:
    def __init__(self):
        print('Constructor is called!')
        print('Self is the object itself', self)


t = TestClass()
t1 = TestClass()


class Table:
    def __init__(self, legs):
        print('New table has {} legs'.format(legs))


t = Table(4)
t1 = Table(3)


class Chair:
    def __init__(self, color):
        self.color = color


c = Chair('green')
print(c, c.color)

c1 = Chair('Red')
print(c1.color)
print('variable c did not change', c.color)
