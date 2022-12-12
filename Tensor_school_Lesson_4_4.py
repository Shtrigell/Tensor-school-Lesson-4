inventory={"Дубовый щит":100, "Пика":150, "Кольцо Баюма":150}
weight=0
while True:
    choice=input("""Выберите действие:
    1. Посмотреть содержимое
    2. Добавить предмет
    3. Удалить предмет
    4. Выйти из инвентаря
    *- При добавлении предмета учитывайте, что максимальный вес равен 1000 единиц
    """)
    weight=sum(inventory.values())
    print("Текущий вес: ", weight,"/1000")
    if choice=="1":
        for key, value in inventory.items():
            print("{0}: {1}".format(key,value))
    elif choice=="2":
        inventory[input("Введите название предмета: ")]=int(input("Введите его вес: "))
    elif choice=="3":
        inventory.pop(input("Введите название удаляемого предмета: "),["Предмет не найден"])
    elif choice =="4":
        break
    else:
        print("Неизвестная команда")
