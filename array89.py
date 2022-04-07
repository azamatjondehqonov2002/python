list=[]
n=int(input("n = "))
for x in range (n):
    k=int(input())
    list.append(k)
i=0
k=True
while k:
    if list[i]>list[i+1]:
        k=False
    i+=1
i-=1
if list[i]<list[i+2]:
    while list[i-1]>list[i] and i>=0:
        list[i], list[i-1]=list[i-1],list[i]
        i-=1
else:
    while list[i+1]<list[i] and i>=0:
        list[i+1], list[i]=list[i],list[i+1]
        i+=1

print(list)