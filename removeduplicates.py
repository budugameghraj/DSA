a=[1,1,2,2,2,3,3]
s=[]
k=0
for i in a:
    if i not in s:
        s.append(i)
print(s)
