def pal():
    s=input("enter the string")
    n=len(s)
    m=s[n::-1]
    if(s==m):
        print(s,"palindrome")
    else:
        print(s,"not a palindrome")   
pal()        