filename = input("Enter your filename: ")
file = open(filename, 'r')
res = open("titled_text.txt", "w")
for line in file:
    res.write(line.title())

