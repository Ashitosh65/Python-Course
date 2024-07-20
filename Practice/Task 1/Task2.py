# Write a Python Program to check whether the given number is divisible by 13 or not
num=120
if(num%13==0):
    print(True)
else:
    print(False)

# Write a Python Program to check whether the given number is divisible by 5 and 6
if(num%5==0 and num%6==0):
    print(True)
else:
    print(False)
# Write a Python Program to check whether the given number is divisible by 10 or 15
if(num%10==0 or num%15==0):
    print(True)
else:
    print(False)

# Write a Python program to reverse a two digit number

x=23
y=int(x/10)
z=x%10
x=z*10+y

print(x)

# Write a Python program to reverse a three digit number

x=231
y=int(x/10)
z=x%10
a=y%10
b=int(y/10)
x=z*100+a*10+b

print(x)