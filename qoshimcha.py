n = int(input("n = "))

for i in range(n):
    for j in range(n):
        if i==j or i==n-1-j:
            print(" 1 ", end = " ")
        elif i<n-j and j>i:
            print(" 2 ", end = " ")
        elif i<n-j and i>j:
            print(" 3 ", end=" ")
        elif i>n-1-j and j>i:
            print(" 4 ", end=" ")
        else:
            print(" 5 ", end=" ")
    print(" ")