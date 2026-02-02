n=int(input("Enter the number of elements : "))
a=[]
for i in range(n):
    x=int(input("Enter the elemt : "))
    a.append(x)
print(a)
max=a[0]
secondmax=0
for i in range(len(a)):
    if a[i]>max:
        secondmax=max
        max=a[i]
    else:
        if a[i>secondmax]:
            secondmax=a[i]
print(secondmax)