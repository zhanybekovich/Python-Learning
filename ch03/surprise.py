import random

surprise1 = "Билет в кино" 
surprise2 = "Поход в горы"
surprise3 = "Ламборгини"
surprise4 = "Самолет"
surprise5 = "Полет на Луну"

surprise = random.randint(1, 5)
if surprise == 1:
    print(surprise1)
elif surprise == 2:
    print(surprise2)
elif surprise == 3:
    print(surprise3)
elif surprise == 4:
    print(surprise4)
elif surprise == 5:
    print(surprise5)
else:
    print("Сюрпризов нет!")
