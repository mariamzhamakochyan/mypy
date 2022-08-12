filename1 = input("Enter your filename: ")
file1 = open(filename1, 'r')
filename2 = open("Enter your filename, you wanna write the titled text:"
file2 = open(filename2, 'w')
for line in file1:
    file2.write(line.title())

