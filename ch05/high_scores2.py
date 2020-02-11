scores = []
choice = None
while choice != "0":
    print(
        """
        Рекорды
        0 - Выйти
        1 - Показать рекорды
        2 - Добавить рекорд
        """
    )
    choice = input("Ваш выбор: ")
    if choice == "0":
        print("До свидания!")
    elif choice == "1":
        print("Рекорды")
        print("Имя\tРезультат")
        for entry in scores:
           score, name = entry
           print(name, "\t", score) 
    elif choice == "2":
        name = input("Впишите имя игрока: ")
        score = int(input("Впишите его результат: "))
        entry = (score, name)
        scores.append(entry)
        scores.sort(reverse=True)
        scores = scores[:5]
    else:
        print("Извините, в меню нет пункта", choice)
input("\n\nНажмите enter, чтобы выйти.")