count = 0
filename = input("Enter your filename :")
file = open(filename, 'r')
for symbols in file:
    count += len(symbols)
print(count)
