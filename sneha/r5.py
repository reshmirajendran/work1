i=0
sum=0
list=[]
avg=0
while i<5:
    a=int(input("enter the number"))
    list.append(a)
    sum+=list[i]
    print(sum)
    i=i+1
    print(list)
avg=sum/5
print("average:",avg)

