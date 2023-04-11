i=0
m=[]
list=[1,2,3,4,5,2,4]
n=len(list)
while i<n:
  if list[i] not in m:
     m.append(list[i])
  i=i+1
print(m)