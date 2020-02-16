class Critter(object):
    """Virtual Pet"""
    def __init__(self, name):
        print("A new critter has been born")
        self.__name = name
    
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if new_name == "":
            print("Critter's name can't be empty")
        else:
            self.__name = new_name
            print("Name change successful.")

    def talk(self):
        print("\nHello my name is", self.name)

crit = Critter("Bob")
crit.talk()