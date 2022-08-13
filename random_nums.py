import random
filename = input("Enter the file name: ")
new_file = open(filename, 'w')
lst = []
new_lst = []
for num in range(1, 100):
     lst.append(num)
for num1 in range(100, 201):
     new_lst.append(num1)
for num1 in range(1, 2 * 10**9):
     num = new_file.write(str(random.choice(new_lst)))
     num = new_file.write(' ')
     num = new_file.write(str(random.choice(lst)))
     num = new_file.write(' ')
