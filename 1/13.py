a=int(input())
max=a
k=0
while a!=0:
    a=int(input())
    if a==max:
        k+=1
    if a>max:
        max=a
        k=0
else: k+=1
print(k)