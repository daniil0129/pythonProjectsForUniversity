immutable_var = (5, "Неизменяемый", True)
print(immutable_var)

immutable_var[0] = "TypeError"

mutable_list = [None, "Изменяемый", 10]
mutable_list[0] = "Проверка"
print(mutable_list)