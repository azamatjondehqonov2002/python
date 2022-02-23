a=int(input("a="))

s=a*a
l=0
while s!=0:
    l+=s%10
    s//=10

print(l)