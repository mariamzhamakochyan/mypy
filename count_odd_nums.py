sum = 0
list = []
first_num = int(input("Enter the first number: "))
last_num = int(input("Enter the last number: "))
for i in range(first_num, last_num + 1):
    list.append(i)
    if i % 2 != 0:
       sum += i
print(f"Sum of odd numbers is {sum}")
       
