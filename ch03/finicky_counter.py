count = 0
while True:
    count += 1
    # завершить цикл, если count принимает значение больше 10
    if count > 10:
        break
    # пропустить 5
    if count == 5:
        print("пять - пять")
        continue
    print(count)