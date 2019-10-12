first_answer = input("Введите элементы первого списка через запятую: ")
first_list = first_answer.split(",")
print("Вот введенный вами первый список:", first_list)

second_answer = input("Введите элементы второго списка через запятую: ")
second_list = second_answer.split(",")
print("Вот введенный вами второй список:", second_list)

i = 0
while i < len(first_list):
    item = first_list[i]
    if item in second_list:
        for j in range(first_list.count(item)):
            first_list.remove(item)
    else:
        i = i + 1
print("Вот модифицированный список:", first_list)