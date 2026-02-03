a=[1,1,2,2,2,3,3]
s=set()
k=0
for i in a:
    s.add(i)
    a[k]=i
    k+=1
print(a)