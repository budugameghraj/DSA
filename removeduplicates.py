a=[1,1,2,2,2,3,3]
s=set()
k=0
for i in range(len(a)):
    s.add(a[i])
    a[k]=a[i]
    k+=1
print(a)
    