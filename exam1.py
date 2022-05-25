#1-masala
n=int(input("n = "))
list1 = []
list2=[]
for x in range (n):
    k=int(input())
    list1.append(k)
for x in range(n):
    if list1[x:].count(list1[x])==1:
        list2.append(list1[x])
print(list2)