
i=0
string=input("enter the string")
even=[]
n=len(string)
while i<n:
    if (i%2==0):
        even.append(string[i])
    i=i+2
print(even)
