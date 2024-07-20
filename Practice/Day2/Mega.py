# Write a python program to print 1-100 numbers in reverse order with a difference of 3 using while loop
num=100
while(num>0):
    print(num)
    num-=3

# Write a python program to print even numbers between 1-200

for i in range(1,201):
    if(i%2==0):
        print(i)

# Write a pythom program to print fibonacci series

num=int(input("Enter a num till which you want fibonacci series: "))
a=0
b=1
print(a,b,end=" ")
while(num>0):
    c=a+b
    a=b
    b=c
    num-=1
    print(c,end=" ")
print("\n")

# Write a pyhton program to check whether the given number is armstrong or not
num=int(input("Enter a number"))
temp=num
arm=0
while(num>0):
    n=num%10
    arm=n**3+arm
    num=int(num/10)
if(arm==temp):
    print("Armstrong")
else:
    print("Not Armstrong")

# Write a python aprogram to generate electricity bill till user choice(first 200 units free,200-500 at 5rs/unit and 500+10rs/unit)
bill=int(input("Enter number of units"))

if(bill<=200):
    print("Your bill is 0")
elif(bill>200 and bill<=500):
    print("Your bill is ",bill*5)
else:
    print("Your bill is ",bill*10)

