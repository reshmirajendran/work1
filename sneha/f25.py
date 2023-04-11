def prime():
    k=0                    
    n=int(input("enter the numbers:"))
    if (n==0 and n==1):
     print("not prime number")
    else:
      i=2
      while i<n:
        if n%2==0:
         i=i+1
      if k==0: 
         print("prime")  
      else:
         print("not prime")
prime()