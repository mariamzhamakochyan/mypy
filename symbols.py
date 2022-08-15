count = 0
filename = input("Enter your filename :")
file = open(filename, 'r')
file = file.read()
file = file.split()
for words in file:
    count += len(words)
print(count)
