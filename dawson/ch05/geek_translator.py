geek = {
    "404": "Не знать, не владеть информацией. От сообщения об ошибке 404 'Страница не найдена'",
    "Googling": "'Гугление', поиск в Сети сведений о ком-либо.",
    "Keyboard Plaque": "Мусор, который скапливается в клавиатуре компьютера",
    "Link Rot": "Процесс устаревания гиперссылок на веб-страницах.",
}

choice = None

while choice != "0":
    print(
        """
        Переводчик с гикского на русский
        0 - Выйти
        1 - Найти толкование термина
        2 - Добавить термин
        3 - Изменить толкование
        4 - Удалить термин 
        """
    )
    choice = input("Ваш выбор: ")
    if choice == "0":
        print("До свидания!")

    elif choice == "1":
        term = input("Какой термин вы хотите перевести: ")
        if term in geek:
            definition = geek[term]
            print(term, "означает", definition)
        else:
            print("Увы, этот термин мне не знаком.")

    elif choice == "2":
        term = input("Какой термин будем добавлять? ")
        if term not in geek:
            definition = input("Впишите толкование: ")
            geek[term] = definition
            print("Термин добавлен в словарь.")
        else:
            print("Такой термин уже есть, попробуйте изменить его толкование.")

    elif choice == "3":
        term = input("Какой термин будем переопределять? ")
        if term in geek:
            definition = input("Впишите ваше толкование: ")
            geek[term] = definition
            print("Термин переопределен.")
        else:
            print("Такого термина пока нет! Попробуйте добавить его в словарь.")

    elif choice == "4":
        term = input("Какой термин будем удалять? ")
        if term in geek:
            del geek[term]
            print("Удален!")
        else:
            print("Ничем не могу помочь, термина нет в словаре.")
            
    else:
        print("Извините, в меню нет пункта", choice)
input("\n\nНажмите enter, чтобы выйти.")