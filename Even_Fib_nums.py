def fib(num):
    num1 = 0
    num2 = 1
    while num2 < num:
      res = num1 + num2
      num1, num2 = num2, res
    if num2 == num or num1 == num:
      return True
    else:
      return False
    
def evalFibsum(n):
  sum = 0
  for i in range(n):
    if fib(num) and (num % 2 == 0):
      sum += num
  return sum

print(fib(50))
