# class bank:
#      def __init__(self,accno,name,bal):
#           self.num=accno
#           self.name=name
#           self.bal=bal
#      def deposit(self):
#            amt=int(input("enter the amount :"))
#            self.bal+=amt
#            print("balance:",self.bal)
#      def withdraw(self):
#         amt=int(input("enter the amount :"))
#         self.bal-=amt
#         print("balance:",self.bal)
# n=int(input("enter the account number:"))
# m=input("enter the name:")
# p=int(input("enter the balance:"))
# ob=bank(n,m,p)
# print("1.Deposit\n2.withdraw\n")
# ch=int(input("enter the choice:"))

# if ch==1:
#     ob.deposit()
# elif ch==2:
#     ob.withdraw()



class Bank:
    def __init__(self,name,age,gender):
        super().__init__(name,age,gender)
        self.balance = 0

    def deposit(self,amount):
        self.amount = amount
        self.balance = self.balance + self.amount
        print("Account balance has been updated : $", self.balance)

    def withdraw(self,amount):
        self.amount = amount
        if self.amount > self.balance:
            print("Insufficient Funds | Balance Available : $", self.balance)
        else:
            self.balance = self.balance - self.amount
            print("Account balance has been updated : £", self.balance)
    
    def view_balance(self):
        self.show_details()
        print("Account balance: $", self.balance)

def cont():
  input("\n\nPress enter to continue\n\n")

exit = 0
while True:
  name = Bank(input("Enter name: "), int(input("Enter Age: ")), input("Enter Gender: ")) 
  options = input("\n\nwhat would you like to do (enter a number)?\n\n1. Withdraw\n2. Deposit\n3. View Account summary\n4. view balance\n5. Exit \n>>")
  if options == '5':
    exit = 1
    break
  if options == '3':
    name.show_details()
    cont()
  elif options == '4': 
    name.view_balance()
    cont()
  elif options == "1":
    name.withdraw(int(input("How much would you like to withdraw?: ")))
    cont()
  elif options == "2": 
    name.deposit(int(input("How much would you like to deposit?: "))) 
    cont()
