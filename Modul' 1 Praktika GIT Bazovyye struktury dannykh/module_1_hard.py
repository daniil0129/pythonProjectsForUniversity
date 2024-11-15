# Входные данные
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

# Сортировка студентов и подсчет средней оценки каждого студента
students = sorted(students)
grades = [sum(i) / len(i)  for i in grades]

# Формирование итогового словаря
result = {s: g for s, g in zip(students, grades)}

print(result)