# 1.Find the Maximum Element: Write a Python function to find the maximum element in a list
lis=[1,5,3,7,2]

def maximum(lis):
    max=lis[0]
    leng=len(lis)
    i=0
    while(leng>0):
        if(max<lis[i]):
            max=lis[i]
        leng-=1
        i+=1
    print(max)

# maximum(lis)

# 2.Check for prime Number: Write a python function to check if a given number is prime or not.
# num=int(input("Enter Number: "))

def prime(num):
    if(num<=1):
        return False
    if(num>=2):
        if(num==2):
            return True
        i=2
        while(i<=num/2):
            if(num%i==0):
                return False
            i+=1
    return True

# x=prime(num)
# print(x)

# 3. Count Vowels and Consonants: Write a Python function to count the number of vowels and consonants in a given string.
# str=input("Enter a String :")

def vowels_consonants(str):
    leng=len(str)
    str=str.lower()
    countv=0
    countc=0
    i=0
    while(leng>0):
        if(str[i]=='a' or str[i]=='e' or str[i]=='i'or str[i]=='o'or str[i]=='u'):
            countv+=1
        else:
            countc+=1
        i+=1
        leng-=1

    print("Number of vowels : ",countv)
    print("Number of consonants : ",countc)

# vowels_consonants(str)

# 4. Find the Sum of Digits: Write a Python function to find the sum of digits of a given number.

# num=int(input("Enter a Number: "))

def sum_num(num):
    sum=0
    while(num>0):
        n=num%10
        sum=sum+n
        num=int(num/10)
    print(sum)
# sum_num(num)

# 5. Remove Duplicates from a List: Write a Python function to remove duplicates from a given list.
lst=[1,2,4,5,3,6,4,2]

def rem_dup(lst):
    leng=len(lst)
    i=0
    x=[]
    for i in range(len(lst)):
        for j in range(i+1,len(lst)):
            if(lst[i]!=lst[j]):
               x.append(lst[i]) 
    print(x)
rem_dup(lst)





# 6. Reverse Words in a Sentence: Write a Python function to reverse the words in a given sentence.

# 7. Check for Anagrams: Write a Python function to check if two given strings are anagrams of each other.

# 8. Find Common Elements: Write a Python function to find common elements between two lists.
