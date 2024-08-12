name = "Bogdan"
i = 0

# Task 2
immutable_var = 1, 2, "Key", name               # создание кортежа
print(immutable_var)

# Task 3
# immutable_var[3] = "Sword"                    # Tuples don't support item assignment (из сигналов)
                                                # Невозможно изменить элемент кортежа - он статичен
                                                # (исключение элементы внутри списка, который сам заложен в кортеж)
immutable_var_2 = [1, 2, "Grand"], 5
print(immutable_var_2)

immutable_var_2[0][1] = immutable_var_2[0][2]
immutable_var_2[0][2] = "Hotel"
immutable_var_2[0].append('!!!')                # Добавление 4 индекса в список заложенный внутри кортежа
print(immutable_var_2)

# Task 4                                        # Изменения в списке
mutable_list = []
print(mutable_list)

for i in range(11):
    mutable_list.append(i)
    print(mutable_list)

while i > -1:
    mutable_list.remove(i)
    i -= 1
    print(mutable_list)
print()

mutable_list.extend(["This is the End!", "Thanks!"])

for j in range(2):
    print(mutable_list[j])
