# def list():
#     print("choice of operation")
#     print("Select an operation:\n1) Add\n2) replace\n3) delete\n4) sort")
#     while True:
#         operator= input("Enter your choice of : \n")
#         list=[]
#         n=int(input("enter the numbers:"))
#         for n in range(n):
#               n1=int(input("enter the numbers:"))
#               list.append(n1)
#               if n=='':
#                    break
              

# list()


# l1=[1,2,3,4,5,8]    
# n1=int(input("enter the first number"))
# n2=int(input("enter the second number"))  
# print("Select an operation:\n1) Add\n2) replace\n3) delete\n4) sort")
# c=int(input("select your choice"))
# if c==1:
#    sum=n1+n2
#    print(l1)



l1=[1,2,3,4,5,8]

def add(p):
    a=p
    l1.append(a)
    print(l1)
def mul(n,m):
    a=n
    b=m
    mul=a*b
    print(l1)   
def rep(p,q):
     a=p
     b=q
     l1[0]=q
     print(l1)
def remove(p,q):
     a=p
     b=q
     del l1[q]
     print(l1)
 
print("choice of option")
print("Select an operation:\n1) Add\n2) mull\n3) replace\n4) delete\n5)sort")
while True:
        n=int(input("enter the choice:"))
        if n==1:
            p=int(input("enter the elements:"))
            add(p) 
        if n==2:
            p=int(input("enter the 1st number:"))
            q=int(input("enter the 2nd number"))
            mul(p,q)
        if n==3:
            p=int(input("enter the elements"))
            q=int(input("enter the number"))
            rep(p,q)
        if n==4:
             p=int(input("enter the element"))
             q=int(input("removing element"))
             remove(p,q) 
        if n==5: 
             l1.sort()  
             print(l1) 
                                                                       
             break
        


