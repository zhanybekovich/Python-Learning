inventory = (
    "кольчуга",
    "щит",
    "целебное снадобье"
)

print("\nИтак, в вашем арсенале:")
for item in inventory:
    print(item)

print("Сейчас в вашем распоряжении", len(inventory), "предметов.")

if "целебное снадобье" in inventory:
    print("Вы еще поживете и повоюете.")

index = int(input("Введите индекс одного из предметов арсенала: "))
print("Под индексом", index, "в арсенале находится", inventory[index])