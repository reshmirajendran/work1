def string():
   str= input("enter a string:")
   x=len(str)
   for i in range(0,x):
    for j in range(0,i+1):
        print(str[j],end="")
    print()
string()  
