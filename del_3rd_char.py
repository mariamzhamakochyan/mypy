str = list(input("Enter your string: "))
del str[2::3]
str = ''.join(str)
print(str)
