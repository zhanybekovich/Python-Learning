inventory = ()
if not inventory:
    print("Вы безоружены.")
input("\nНажмите Enter, чтобы продолжить.")

inventory = (
    "меч",
    "кольчуга",
    "щит",
    "целебное снадобье"
)

print("\nСодержимое кортежа:")
print(inventory)
for item in inventory:
    print(item)

input("Нажмите Enter, чтобы выйти.")