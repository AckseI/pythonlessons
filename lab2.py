def func(my_list):
    new_list = []
    for i in my_list:
        if i ** 2 >= 1:
            pass
        else:
            new_list.append(i)
    return new_list


my_list = [1, 5, 15, 2, 3, 4]
with open("output_lab2txt", "w") as file:
    for line in func(my_list):
        file.write(str(line) + " ")
