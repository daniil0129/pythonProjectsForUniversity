# Работа со словарями:
my_dict = {
    "Sasha": 1997,
    "Danil": 1995,
    "Vera": 2001
}
print(my_dict)
print(my_dict.get("Safsha"))
print(my_dict.get("Eva", "Данного ключа не существует"))

my_dict.update({
    "Ivan": 1986,
    "Lara": 1990
})
print(my_dict.pop("Vera"))
print(my_dict)

# Работа с множествами:
my_set = {1, "yes", None, 1, 1, 1}
print(my_set)
my_set.update([56, "no"])
my_set.discard(None)
print(my_set)