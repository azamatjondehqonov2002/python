from random import randint

n=int(input("n = "))
s=""
for x in range(n):
    a=randint(1,4)
    if a==1:
        s+="A"
    elif a==2:
        s+="B"
    elif a==3:
        s+="C"
    else:
        s+="D"

print(s)