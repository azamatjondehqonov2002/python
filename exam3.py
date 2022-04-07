#3-masala
def ekub(a,b):
    while a!=b:
        if a>b:
            a-=b
        else:
            b-=a 
    return a   

n=int(input())
ekuk=int(input())
for x in range(1,n):
    k=int(input())
    ekuk=ekuk*k/ekub(ekuk,k)

print(ekuk)