# Create a var num and assign 4+2; using complex function.Print val of num and its datatype
num=complex(4,2)
print(num)

# Check given num is larger than 23
num=32
if(num>23):
    print(True)
else:
    print(False)

# Check given num is less than or equal to 40
num=78
if(num<=40):
    print(True)
else:
    print(False)

# Check given num is not equaal to 10
if(num!=10):
    print(True)
else:
    print(False)

# Take a variable,assign marks and update var by adding 30 to it
marks=40
print(int(marks)+40)

# Take firstname,lastname from commandline and print them along with file name
import sys
firstname=sys.argv[1]
lastname=sys.argv[2]

print(firstname)
print(lastname)

# Take firstname,lastname from keyboard and print them 
firstname=input("Enter Firstname: ")
lastname=input("Enter lastname: ")
print(firstname)
print(lastname)

# Take 2 integer from keyboard and print sum
num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))

print(num1+num2)
