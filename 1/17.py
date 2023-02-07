from math import sqrt
count  = -1
sum = 0
sum_kv = 0
x = 1
while x != 0:
    x = int(input())
    sum += x
    sum_kv += x*x
    count += 1
s = sum / count
b = sqrt((count*s*s - 2*s*sum + sum_kv) / (count - 1))
print(b)