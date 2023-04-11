# class number:
#   x = 5

# p1 = number()
# print(p1.x)


# class age:
#     x=20
# p1=age() 
# print(p1.x)   



# class person:
#     def __init__(self, name, age):
#      self.name=name
#      self.age=age
# p1=person("john",36)
# print(p1.name)
# print(p1.age)



# class person:
#     def __init__(details,name,age):
#         details.name=name
#         details.age=age
#     def __str__(details):
#         return f"{details.name}({details.age})"
# p1=person("john",30)
# print(p1)


# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

#   def myfunc(self):
#     print("Hello my name is " + self.name)
   

# p1 = Person("John", 36)
# p1.myfunc()

# class student: 
#     def __init__(self, name, age,place,branch):
#         self.name=name
#         self.age=age
#         self.place=place
#         self.branch=branch
#     def __str__(self):
#          return f"{self.name},({self.age}),{self.place},{self.branch}"
# n=int(input("register number:"))
# p1=student("appu","20","tvm","computer science")
# print(p1.name)
# print(p1.age)
# print(p1.place)
# print(p1.branch)




# class bank:
#     def __init__(self,accno,name,bal):
#         self.num=accno
#         self.name=name
#         self.bal=bal
#     def deposit(self):
#         amt=int(input("enter the amount :"))
#         self.bal+=amt
#         print("balance:",self.bal)
#     def withdraw(self):
#         amt=int(input("enter the amount :"))
#         self.bal-=amt
#         print("balance:",self.bal)
# n=int(input("enter the account no:"))
# m=input("enter the name:")
# b=int(input("enter the balance:"))
# ob=bank(n,m,b)
# print("1.Deposit\n2.withdraw\n")
# ch=int(input("enter the choice:"))

# if ch==1:
#     ob.deposit()
# elif ch==2:
#     ob.withdraw()
class bank:
    def __init__(self,accno,name,bal):
        self.num=accno
        self.name=name
        self.bal=bal
    def deposit(self):
        amt=int(input("enter the amount :"))
        self.bal+=amt
    def withdraw(self):
        amt=int(input("enter the amount :"))
        self.bal-=amt
    def  showbal(self):
        print(self.bal)
l=[]
while True:
  print("1.create\n2.deposit\n3.withdraw\n4.show balance\n5.exit\n")
  ch=int(input("enter the choice"))
  if ch==1:
      n=int(input("enter account no:"))
      m=input("enter the name:")
      b=int(input("enter the balance:"))
      ob=bank(n,m,b)
      l.append(ob)
  if ch==2:
    accno=int(input("enter accno:"))
    for i in l:
        if i.num==accno:
             i.deposit()
  if ch==3:
    accno=int(input("enter accno:"))
    for i in l:
        if i.num==accno:
             i.withdraw()

  if ch==4:
      accno=int(input("enter accno:"))
      for i in l:
        if i.num==accno:
             i.showbal()

      
      
