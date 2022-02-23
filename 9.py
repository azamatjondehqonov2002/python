x=float(input("x = "))
y=float(input("y = "))
a=float(input("a = "))
b=float(input("b = "))
c=float(input("c = "))
if x>=a and (y>=b or y>=c):
    print("Sig'adi")
elif x>=b and (y>=a or y>=c):
    print("Sig'adi")
elif x>=c and (y>=a or y>=b):
    print("Sig'adi")
else:
    print("Sig'maydi")