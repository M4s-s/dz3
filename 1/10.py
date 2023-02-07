x=int(input())
k=0
if x%2==0:
    k+=1
while x!=0:
    x=int(input())
    if x%2==0:
        k+=1
print(k-1)
