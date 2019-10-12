answer = input("Введите элементы списка через запятую: ")
list = answer.replace(";", ",").replace("/", ",").split(",")
print("Вот введенный вами список:", list)
i = 0
while i < len(list):
    item = list[i]
    if list.count(item) > 1:
        for j in range(list.count(item)):
            list.remove(item)
    else:
        i = i + 1
print("Вот модифицированный список:", list)