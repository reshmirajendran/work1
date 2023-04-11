#amstrong

n= int(input("Enter a number: "))
sum=0
t=n
while t>0:
        digit = t % 10
        sum += digit ** 3
        t//= 10
if n == sum:
    print(n,"amstrome number")
else:
    print(n,"not an amstrome")

