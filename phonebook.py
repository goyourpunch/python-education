# PHONE BOOK!
phone_book = {}

while True:
    print("\n Меню")
    print("1. Добавить контакт")
    print("2. Найти контакт")
    print("3. Удалить контакт")
    print("4. Список всех контактов")
    print("5. Выйти")
    
    choice = input("Выбери действие:")
    
    if choice == "1":
        name = input("Введите имя: ")
        phone = int(input("Введите номер телефона: ")) #добавить else чтобы говорило что нужно ввести цифры а не буквы
        phone_book[name] = phone
        print("Контакт добавлен!")
    elif choice == "2":
        name = input("Введите имя: ")
        if name in phone_book:
            print("Номер телефона", phone_book[name])
        else:
            print("Контакт не найден")
    elif choice == "3":
        name = input("Введите имя контакта для удаления: ")
        if name in phone_book:
            print(f"Контакт {name} удалён. ")
        else:
            print("Контакт не найден.")
    elif choice == "4":
        if phone_book:
            print("\nСписок контактов:")
        for name, phone in phone_book.items():
            print(f"{name}:{phone}")
    elif choice == "5":
        print("Выход")
        break
    else:
        print("Неверный выбор. Попробуйте снова.")