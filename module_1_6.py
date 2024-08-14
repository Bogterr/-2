# Task 2
print("*" * 30)
print("Задание N°2")
print("*" * 30)
my_dict = {"Понедельник": 1, "Вторник": 2, "Среда": 3, "Четверг": 4, "Пятница": 5, "Суббота": 6, "Воскресенье": 7}
print("Словарь: ", my_dict)
print()

print("Значение ключа 'Понедельник': ", my_dict.get("Понедельник"))
print("Значение ключа 'Фамилия': ", my_dict.get("Фамилия"))
print()

my_dict.update({"Monday": 1, "Tuesday": 2, "Wednesday": 3, "Thursday": 4, "Friday": 5, "Saturday": 6, "Sunday": 7})
print("Обновленный словарь: ", my_dict)
print()

x = my_dict.get("Воскресенье")
my_dict.pop("Воскресенье")
print("Вырезан item 'Воскресенье': ", my_dict)
print()
print("Значение, удаленного из словаря ключа, 'Воскресенье': ", x)
# ********************

print("*" * 30)
# Task 3
print("Задание N°3")
print("*" * 30)
my_set = {1, 1, 2, 2, 1, 14, 20, 20, 5, 6, 2024, 8, 8, 1, 1, 5}

print("Множество: ", my_set)
print()

my_set.update((9, 10, 19))         # добавление элементов

print("Новое множество: ", my_set)
print()

my_set.remove(8)                    # удаление символа
print("8 Удалено из множества", my_set)
print()
# ********************

# Special task
print("*" * 30)
print("Special task")
print("*" * 30)
my_list = {1, 8, 2, 2, 1, 14, 20, 9, 1, "Igor", "Semen"}
print(my_list)

for i in range(100):      # для i в диапазоне от 0 до 100
    if i not in my_list:    # если i не входит в my_list
        my_list.add(i)        # добавить i в my_list

print(my_list)
print(len(my_list))
print()
