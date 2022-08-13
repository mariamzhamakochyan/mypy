sum = 0
num = 0
filename = input("enter the file name: ")
file = open(filename, 'r')
for line in file:
    num = str(line)
    sum += int(num)
print(sum)
