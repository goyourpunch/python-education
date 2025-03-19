phone_book = {}  # Словарь для хранения контактов

if choice == 1:
    while True:  # Цикл добавления контакта
        while True:  # Ввод имени
            name = input("Введите имя: ")
            if name.isalpha():
                break
            else:
                print("Ошибка: имя должно содержать только буквы. Попробуйте снова.")

        while True:  # Ввод номера телефона
            phone = input("Введите номер телефона: ")
            if phone.isdigit():
                # Проверяем, существует ли этот контакт полностью (имя + номер)
                if phone_book.get(name) == phone:
                    print(f"Контакт {name} с номером {phone} уже существует!")
                    break  # Возвращаемся к новому контакту

                # Проверяем, существует ли номер, но с другим именем
                existing_name = None
                for contact_name, contact_phone in phone_book.items():
                    if contact_phone == phone:
                        existing_name = contact_name
                        break

                if existing_name and existing_name != name:  # Номер есть, но с другим именем
                    print(f"Этот номер уже записан для контакта {existing_name}. Хотите объединить?")
                    while True:
                        merge_action = input("\nВыберите действие: \n1 - Да \n0 - Нет\nВаш выбор: ")
                        if merge_action == "1":
                            new_name = f"{name} ({existing_name})"  # Добавляем старое имя в скобки
                            phone_book[new_name] = phone  # Записываем новый контакт
                            del phone_book[existing_name]  # Удаляем старый контакт
                            print(f"Контакты объединены. Теперь {new_name} имеет номер {phone}.")
                            break
                        elif merge_action == "0":
                            print("Контакт не изменён.")
                            break
                        else:
                            print("Ошибка: введите 1 или 0.")

                else:  # Если номера ещё нет в телефонной книге
                    phone_book[name] = phone
                    print(f"Контакт {name}: +{phone} добавлен!")

                break  # Выходим из ввода номера
/////////////////////////////////////////////////////////////
            else:
                print("Ошибка: номер телефона должен содержать только цифры. Попробуйте снова.")

        while True:  # Выбор дальнейших действий
            action = input("\nВыберите действие: \n1 - Добавить ещё один контакт \n0 - Вернуться в меню\nВаш выбор: ")
            if action == "1":
                break  # Начинаем заново (новый контакт)
            elif action == "0":
                exit_loop = True  # Флаг для выхода
                break
            else:
                print("Ошибка: введите 1 или 0.")

        if "exit_loop" in locals() and exit_loop:
            break  # Полностью выходим в главное меню
