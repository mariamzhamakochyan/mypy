def data(lst):
    list = []
    for i in lst:
        i = i ** 2
        list.append(i)
    for i in range(0, len(list)):
        for j in range(i + 1, len(list)):
            if list[i] > list [j]:
               list[i], list[j] = list[j], list[i]
    return list
lst = [-7, 11, 2, 3, 4, 5]
print(data(lst))
