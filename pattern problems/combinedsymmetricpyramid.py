n=int(input("Enter a number : "))
for i in range(n):
    for j in range(n-i):
        print(" ",end=" ")
    for j in range(2*i+1):
        print("*",end=" ")
    print()
for k in range(n-1,0,-1):
    print(" ",end=" ")
    for l in range(n-k):
        print(" ",end=" ")
    for l in range(2*k-1):
        print("*",end=" ")
    print()