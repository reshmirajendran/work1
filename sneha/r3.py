i=0
sum=0
list=[1,2,3,4,5]
n=len(list)
while(i<n):
    sum+=list[i]
    i+=1
    print("sum of list",sum)   
average = sum / n
print("Average=",average)