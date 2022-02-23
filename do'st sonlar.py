#Do'st sonlar
n=int(input())

for x in range(1,n):
    s1=0
    s2=0
    for k in range(1,x):
        if x%k==0:
            s1+=k
    if x>s1:
        for k in range(1,s1):
            if s1%k==0:
                s2+=k
    if s2==x and x!=s1:
        print(s1,", ", x)