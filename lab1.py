def func(my_list):
    new_array = []
    for i in my_list:
        if i == 13:
            return new_array
        else:
            my_list = new_array.append(i)

array = [1, 2, 3, 13, 4]
print(sum(func(array)))
