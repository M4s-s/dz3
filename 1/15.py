n1=0
n2=1
k=1
a=int(input())
while n2<a:
    n1,n2=n2,n2+n1
    k+=1
if n2!=a:
    print("-1")
else:
    print(k)
