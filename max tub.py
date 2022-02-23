# tub sonlar maksimali
n=int(input())
tub=0
for x in range(n):
    k=int(input())
    tub1=True
    for a in range(2,k):
        if k%a==0:
            tub1=False
            break
    if tub1 and k>tub:
        tub=k

if tub>1:
    print(tub)
else:
    print("Tub son kiritilmadi")