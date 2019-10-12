list = []
count = int(input("Введите число элементов в списке:"))
for i in range(count):
    print("Введите", i + 1, "элемент.")
    item = int(input("Ваш элемент:"))
    list.append(item)
list.sort()
print(list)