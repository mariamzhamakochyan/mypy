def data(list):
    dict = {}
    keys = dict.keys()
    for i in list:
        if i in keys:
           dict[i] += 1
        else:
           dict.update({i:1})
    return dict
list = [1, 2, 5, 7, 8, 9, 1, 1, 2, 5]
print(data(list))
