row = input("Enter your string: ")
position = int(input("Enter the numbe of displacement: "))
def strmove(row):
    dis = row[0:position]
    row_ = row[position:]
    res = row_ + dis
    return res
print(strmove(row))
