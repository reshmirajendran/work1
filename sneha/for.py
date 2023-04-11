fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x) 
for x in "banana":
  print(x) 


list=[]
for n in range(1500, 2100):
    if (n%7==0 and n%5==0 ):
         list.append(n)
print(list)


string = input("enter the string")
for i in string:
    if (string.index(i))%2==0:
        print(i)

n = 11
for i in range(1,n):
        print(i)


n=20
for i in range(n):
   if i%2==0:
       print(i)
 