def sum_num(n):
    sum = 0
    while n != 0:
          sum += n % 10
          n = n // 10
    return sum
n = 4637
print(sum_num(n))
