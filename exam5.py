n=int(input("n = "))
min=0
for x in range (n):
    k=float(input())
    if k>0:
        if min!=0: 
            if min>k:
                min=k
        else:
            min =k

if min!=0:
    print("Kiritilgan sonlar ichida eng kichik musbat son bu ",min)
else:
    print("musbat son kiritilmadi.")