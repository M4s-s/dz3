n = int(input())
if n == 0:
    print(0)
else:
    x = 0
    new = 1
    for i in range(2, n + 1):
         x, new = new, new + x
    print(new)
