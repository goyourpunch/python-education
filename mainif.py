# age = int(input("what is your age?"))

# if age >= 21:
#     print("вы взрослый") #если возраст больше 21 или равен 21, значит что вы взрослый
# elif 18 <= age > 20:
#     print("вам нужно ещё подрости") #если возраст больше/равен 18 но не больше 20
# else:
#     print("access denied!") #если возраст меньше 18, доступ запрещён


# age = int(input("Введите ваш возраст: "))

# if age < 13:
#     print("Вы ребёнок.")
# elif 13 <= age < 18:
#     print("Вы подросток.")
# elif 60 <= age:
#     print("Вы старый.")
# elif age == 25:
#     print("Сейчас 2025 год.")
# else:
#     print("Вы взрослый.")


# age = int(input("Введите ваш возраст: "))

# if 1 <= age < 13:
#     print("Вы ребёнок.") #Если возраст от 1 до 13 лет, выводится сообщение "Вы ребёнок".
# elif 13 <= age < 18:
#     print("Вы подросток.") #Если возраст от 13 до 17 лет (включительно), выводится сообщение "Вы подросток".
# elif age == 0:
#     print("ты ещё не родился?))")
# elif 18 <= age <= 21: #если возраст от 18 до 21 лет (включительно), выводиться "покупай алкоголь".
#     print("покупай алкоголь")
# elif age == 55:
#     print("сейчас 2055") #если возраст равен 55, сейчас 2055год!
# elif 56 < age <= 100:
#     print("сейчас будещее")
# elif 44 >= age < 40:
#     print("соси")
# else:
#     print("Вы взрослый.") #Если возраст 18 лет и больше, выводится сообщение "Вы взрослый".



# age = int(input("what your age?"))

# if age > 18:
#     print("access grandet!")
# elif 14 <= age < 18:
#     print("подросток")
# elif 19 < age < 40:
#     print("old")
# else:
#     print("access denied!")


print("Привет, я хочу узнать тебя побольше")
print("хочешь пройти небольшой тест?")
answer = str(input()) # сохраняем ответ пользователя в переменную
if answer == "да": # сравниваем переменную с "yes"
    print("хорошо, давай начнем")

    print("what your name?") 
    name = str(input())
    if name == "Миша":
        print("мне очень нравиться имя,", name) #понравился ответ и сработало другое условие

        print("сколько тебе лет", name, "?")
        age = int(input())
        if age >= 30:
            print("чего ты добился в свои", age, "старик?")
        elif 18 <= age < 30:
            print("ты мечтаешь о машине?")
            
            answercar = str(input())
            if answercar == "да":
                print("это очень хорошо)))")

                print("а о какой машине мечтаешь", name)
                car = str(input())
                if car == "BMW":
                    print("давай займёмся сексом в ней!!!")

            else:
                print("я не знаю, что сказать...")

        elif age < 18:
            print("ты слишком маленький", name, "!!!")
        else:
            print("я не знаю, что сказать...")

    elif name == "Дима":
        print(name, "?", "у меня так брата зовут!)")

        print("какой ты национальности?", name)
        nationality = str(input())
        if nationality == "Украина":
            print("мне очень нравиться", nationality)
        elif nationality == "usa":
            print("I want children from you!")
        else:
            print("фу урод!")

    else:
        print("хорошее имя,", name)
elif answer == "ДА":
    print("не пиши капсом баран!")
else:
    print("ты тупой сорри")