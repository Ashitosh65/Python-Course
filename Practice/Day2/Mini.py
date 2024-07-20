# Write the python program to check whether the given number is even or odd
num=10
if(num%2==0):
    print("Even")
else:
    print("Odd")

# Write the python program to provide discount of 10% on bill amount if
# and only if when bill is greater than 10000/-

bill=int(input("enter bill: "))

if(bill>10000):
    bill=bill-bill/10
    print("You got a dicount of 10% and your new bill is = ",bill)
else:
    print("You don't have any dicount and your bill is :",bill)

# Write a python program to check whether a given 3digited number is palindrome or not

num=int(input("Enter number for pal: "))
a=int(num%10)
b=int(num/10)
c=int(b/10)

if(a==c):
    print("Palindrome")
else:
    print("Not Palindrome")

# Write python program to accept citizenship.if he is "Indian" then only ask for his age.Now check whether he is major or minor,if he is not indian then display the message "Not for others"

citizenship=input("Enter Citizenship: ")
if(citizenship=="Indian"):
    age=int(input("Enter age:"))
    if(age>=18):
        print("You are major")
    else:
        print("You sre minor")
else:
    print("Not for Others")

