

# def python():
#  s=input("enter the string")
#  n=len(s)
#  for i in range(0,2):
#    print(s[i],end=" ")
#  for i in range(n-2,n):
#    print(s[i],end=" ")
#    print()
# python()    

# s="python"
# n=len(s)
# for i in range(0,2):
#       print(s[i],end=" ")
# for i in range(n-2,n):
#    print(s[i],end=" ")
#    print()
    

l=input("enter the string")

s=l[:1]+l[-2:]
n=len(s)
for i in range(len(s)):
    print(s[i]+".", end=" ")
print()