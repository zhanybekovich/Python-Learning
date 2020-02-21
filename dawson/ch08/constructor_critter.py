class Critter(object):
    """Виртуальный питомец"""
    def __init__(self, name):
        print("Появилась на свет новая зверюшка!")
        self.name = name
    
    def __str__(self):
        rep = "Объект класса Critter\n"
        rep += "имя: " + self.name + "\n"
        return rep
    
    def talk(self):
        print("\nПривет, Меня зовут", self.name, "\n")

crit1 = Critter("Бобик")
crit1.talk()

crit2 = Critter("Мурзик")
crit2.talk()

print(crit1)
print(crit1.name)
