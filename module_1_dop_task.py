# Задание "Средний балл"
print("Задание 'Средний балл'")
print()

grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
sr_bal = []
sr_bal_v2 = []
ready_journal = {}
ready_journal_v2 = {}                           # для 2го варианта решения (округление)

print(grades)
print(students)
print()

students = sorted(students)                     # sorted списка учеников по алфавиту
print(students)


for i in range(len(grades)):                    # прогон по списку учеников. Сколько учеников, столько оценок?))
    sum_ = 0                                    # для суммы всех оценок
    count = 0                                   # количество оценок
    aver_sum = 0                                # средний балл
    aver_sum_v2 = 0                             # средний балл (округленный)
    for j in range(len(grades[i])):
        sum_ += grades[i][j]
        count += 1
        aver_sum = sum_/count                   # средний балл, дробный
        aver_sum_v2 = round(sum_/count)         # округление, как в учеб.заведении до ближайшего целочисленного значения
    # print(aver_sum)
    # print(aver_sum_v2)
    sr_bal.append(aver_sum)                     # ср.сумма дробная добавленная в список
    sr_bal_v2.append(aver_sum_v2)               # ср.сумма округленная добавленная в список

# print(sr_bal)
print()

# print(students)
# print(sr_bal)

i = 0                                           # сбросил счетчики на всякий случай (для чистоты счета)
j = 0
k = 0

for i in range(len(students)):                  # снова прогон по списку студентов
    j = students[i]                             # переменной j присвоил имя из списка
    k = sr_bal[i]                               # переменной k присвоил средний балл дробный
    # print(j)
    # print(k)
    ready_journal[j] = k                        # заполнение словаря дробным ср.баллом

    k = sr_bal_v2[i]                            # переменной k присвоил средний балл округленный
    ready_journal_v2[j] = k                     # заполнение словаря округленным ср.баллом

print(ready_journal)
print(ready_journal_v2)
