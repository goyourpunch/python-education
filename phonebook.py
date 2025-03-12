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
    
    if not choice.isdigit():  # Проверка, что введена цифра
        print("Ошибка: введите номер действия (1-5).")
        continue
    
    choice = int(choice)    # Преобразуем в число
    
    if choice == 1:
        while True: # Цикл добавления контакта
            while True: # Бесконечный цикл для проверки str в имени # Цикл для ввода имени
                name = input("Введите имя: ")
                if name.isalpha(): # Проверяем, что имя состоит только из str # Проверяем, что имя содержит только буквы
                    break # Если ввод корректный, выходим из цикла
                else:
                    print("Ошибка: имя должно содержать только буквы. Попробуйте снова.")
                    
            while True: # Бесконечный цикл для проверки номера телефона
                phone = input("Введите номер телефона: ")
                if phone.isdigit(): # Проверяем, что номер состоит только из int
                    phone_book[name] = phone
                    print(f"Контакт {name}: +{phone} добавлен!")
# ////////////////////////////////////////////////////////////////////////////                    # / /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                    while True:
                        action = input("\nВыберите действие: \n1 - Добавить ещё один контакт \n0 - Вернуться в меню\nВaш выбор: ")
                        if action == "1":
                            break # Начинаем заново (новый контакт)
                        elif action == "0":
                            exit_loop = True # Флаг для выхода
                            break
                        else:
                            print("Ошибка: введите 1 или 0.")
                    
                    if "exit_loop" in locals() and exit_loop: # Выходим в главное меню
                        break
                else:
                    print("Ошибка: номер телефона должен содержать только цифры. Попробуйте снова.")
    elif choice == 2:     #если такого контакта не найденно предложить весь список контактов 
        while True:
            query = input("Введите имя или номер: ")
            if query.isalpha() or query.isdigit():
                break
            else:
                print("Ошибка: ввод должен содержать только буквы(имя) или цифры (номер). Попробуйте снова.")
                
        if query in phone_book:
            print(f"Номер телефона: {phone_book[query]}")
            
        elif query in phone_book.values():
            for name, number in phone_book.items():
                if number == query:
                    print(f"Этот номер принадлежит: {name}")
                    break
        else:
            print("Контакт не найден")
            
            while True:
                action = input("\nВыберите действие: \n1 - Найти контакт\n2 - Список всех контактов\n0 - Вернуться в меню\nВаш выбор:")
                if action == "1":
                    break # Начинаем заново (новый контакт)
                elif action == "2":
                    if phone_book: #Если словарь не пустой
                        print("\nСписок контактов:")
                        for name, phone in phone_book.items():
                            print(f"{name}: +{phone}")
                    else: # Если словарь пустой
                        print("Список контактов пуст")
                elif action == "0":
                    exit_loop = True #Флаг для выхода
                    break
                else:
                    print("Ошибка: введите 1, 2 или 0.")
    elif choice == 3:
        query = input("Введите имя или номер контакта для удаления: ")

        if query in phone_book:
            del phone_book[query]
            print(f"Контакт {query} удалён.")

        else:
        # Проверяем, является ли ввод номером, и ищем его в словаре
            name_to_delete = None
            for name, number in phone_book.items():
                if number == query:
                    name_to_delete = name
                    break

            if name_to_delete:
                del phone_book[name_to_delete]
                print(f"Контакт {name_to_delete} (номер {query}) удалён.")
            else:
                print("Контакт не найден.")
    elif choice == 4:
        if phone_book: # Если словарь не пустой
            print("\nСписок контактов:")
            for name, phone in phone_book.items():
                print(f"{name}: +{phone}")
        else: # Если словарь пустой
            print("Список контактов пуст.")
    elif choice == 5:
        print("Выход")
        break
    else:
        print("Неверный выбор. Попробуйте снова.")
        
        
        