
import re

str= input("enter the string:")


x = re.findall("[a-zA-Z]*[0-9]*[_]", str)

print(x)

if x:
  print("Yes, match")
else:
  print("No match")              