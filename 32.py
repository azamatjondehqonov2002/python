#for optimal
n=int(input())
for x in range(n):
    i=0
    a=x
    m=True
    for k in range(n):
        print(a%n,end=" ")
        if m and a%n!=0:
            a-=1
                        
        else:
            a+=1
            m=False
    print(" ")