print("Я готов к счету!")
start = int(input("С какого числа начнем считать? "))
end = int(input("До какого числа нужно посчитать включительно? "))
stepping = int(input("Шаг счета? "))

for number in range(start, end, stepping + 1):
    print(number)