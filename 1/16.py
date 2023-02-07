prev = -1
curr_rep_len = 0
t, m = 1,1
p=1
s=int(input())
while s!=0:
    p , s = s, int(input())
    if p==s:
        t=t+1
    else:
        if t>m:
            m=t
        t=1
print(m)