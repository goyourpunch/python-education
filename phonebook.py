# PHONE BOOK!
phone_book = {}  # Словарь для хранения контактов

while True:
    print("\n Меню")
    print("1. Добавить контакт")
    print("2. Найти контакт")
    print("3. Удалить контакт")
    print("4. Список всех контактов")
    print("0. Выйти")
    
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
                    
            while True: # цикл для проверки номера телефона
                phone = input("Введите номер телефона: ")
                if phone.isdigit(): # Проверяем, что номер состоит только из int
                    # Проверяем, существует ли уже этот контакт с таким же именем и номером
                    if phone_book.get(name) == phone:
                        print(f"Контакт {name} с номером {phone} уже существует!")
                        break # Возвращаемся к вводу нового контакта
                    
                    # Проверяем, существует ли уже этот номер в телефонной книге, но с другим именем
                    existing_name = None
                    for contact_name, contact_phone in phone_book.items():
                        if contact_phone == phone:
                            existing_name = contact_name
                            break
                    
                    
                    if existing_name and existing_name != name: # Номер есть, но с другим именем
                        print(f"Этот номер уже записан для контакта {existing_name}. Хотите обьединить?")
                        while True:
                            merge_action = input("\nВыберите действие: \n1 - Да \n0 - Нет\nВaш выбор: ")
                            if merge_action == "1":
                                new_name = f"{name} ({existing_name})" #Добавляем старое имя в скобки
                                phone_book[new_name] = phone #Записываем новый контакт
                                del phone_book[existing_name] #Удаляем старый контакт
                                print(f"Контакты обьединены. Теперь {new_name} имеет номер {phone}.")
                                break
                            elif merge_action == "0":
                                print("Контакт не изменён.")
                                break
                            else:
                                print("Ошибка: введите 1 или 0.")
                            
                else: # Если номера нет или он уже записан под этим же именем
                    phone_book[name] = phone
                    print(f"Контакт {name}: +{phone} добавлен!")
                    
                # break
                    ///////////////////////////////////////////////////////////////////////////////////
                while True:
                    action = input("\nВыберите действие: \n1 - Добавить ещё один контакт \n0 - Вернуться в меню\nВaш выбор: ")
                    if action == "1":
                        break # Полностью начинаем ввод заново (возвращаемся к имени)
                    elif action == "0":
                        exit_loop = True # Флаг для выхода
                        break
                    else:
                        print("Ошибка: введите 1 или 0.")
                    
                if "exit_loop" in locals() and exit_loop:
                    break # Выход в главное меню
                else:
                    break  # Этот `break` нужен, чтобы выйти из ввода номера и вернуться к имени
                    
            else:
                print("Ошибка: номер телефона должен содержать только цифры. Попробуйте снова.")
            
        if "exit_loop" in locals() and exit_loop:
            break  # Полностью выходим из внешнего цикла       
                
               # при добавлении контакта который уже существует с этим номером, писать что такой номер тлф но с другим именем уже существует, хотите обьединить? 1 - да, 0 - нет, если 1 то (отправлять в скобки имя которое выберу), добавить выбор имени цыфра = имя, какую цыфру ввожу такое имя и будет
               # при добавлении контакта у которого сходятся имя и номер, написать что такой контакт уже существует, и выбор 1 - добавить контакт 0 - главное меню 
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
    elif choice == 0:
        print("Выход")
        break
    else:
        print("Неверный выбор. Попробуйте снова.")
        
        
        