filename = input("Enter the filename: ")
file = open(filename, 'r')
readFile = file.read()
dict = {}
keys = dict.keys()
word = readFile.split()
for i in word:
    if i in keys:
       dict[i] += 1
    else:
       dict.update({i:1})
print(dict)
