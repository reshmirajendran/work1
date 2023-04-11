l1=[1,2,3,4,5,7]
l2=[2,3,9,4,6,7]
n=[]
k=len(l1)
i=0
while i<k:
    if l1[i]%2==0:
        n.append(l1[i])
    elif l2[i]%2!=0:
        n.append(l2[i])
    i=i+1
    n.sort()
print(n)
