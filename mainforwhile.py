# fruits = ["яблоко", "банан", "вишня"]
# for fruit in fruits:
#     print(fruit)  # Выведет каждое слово по очереди


# dierfriend = ["belarus", "nastya", "maks"]
# for friend in dierfriend: #friend это таже переменная к которой приписываеться перечень
#     print(f"сейчас friend = {friend}")  # Выведет каждого друга в столбчик

# for letter in "splash":
#     print(letter)  # Выведет каждую букву по очереди

# number = 1  # Начинаем с 1
# # number = int(input("enter number:"))
# while number <= 5:  # Пока number меньше или равно 5, выполняем код
#     print(number)
#     number += 1  # Увеличиваем number на 1 (иначе цикл будет бесконечным!)


# number = int(input("Введите число (0 для выхода): "))  

# while number != 0:  
#     print(f"Вы ввели: {number}")  
#     number = int(input("Введите число (0 для выхода): "))  # Запрашиваем новое число
#     if number == 0:
#         print("you exit!")
#     else:
#         print("you continue!")


# count = 0
# while count < 5:
#     print("Счётчик:", count)
#     count += 1

name = input("Введите ваше имя: ")
age = int(input("Введите ваш возраст: "))
if age >= 18:
    print(f"{name}, доступ разрешён.")
else:
    print(f"{name}, доступ запрещён.")
# Повторить приветствие 5 раз
for _ in range(5):
    print(f"Привет, {name}!")


