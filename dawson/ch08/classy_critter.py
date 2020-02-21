class Critter(object):
    """Виртуальный питомец"""
    total = 0
    @staticmethod
    def status():
        print("\nВсего зверюшек сейчас", Critter.total)
    
    def __init__(self, name):
        print("Появилась на свет новая зверюшка!")
        self.name = name
        Critter.total += 1

print("Нахожу значение атрибута класса Crittter.total:", end=" ")
print("Создаю зверюшек.")
crit1 = Critter("зверюшка 1")
crit1 = Critter("зверюшка 2")
crit1 = Critter("зверюшка 3")

Critter.status()
print("Обращаюсь к атрибуту класса через объект:", end=" ")
print(crit1.total)

