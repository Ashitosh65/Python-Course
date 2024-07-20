# Using while loop print 10 to 1

num=10
while(num>0):
    print(num)
    num-=1

# Using for loop with list of num,print square of them

lst=[2,3,5,6,7]
for i in lst:
    print(i,"**",2,"=",i**2)

# take len of list from user and take all ele from user and create list

leng=int(input("Length"))
i=0
lst=[]
print("Enter Elements")
while(leng>0):
    ele=int(input())
    lst.append(ele)
    leng-=1
print(lst)



# create dict with taking len and key,val from user
leng=int(input("Length"))
i=0
dic={}
# print("Enter Elements")
while(leng>0):
    key=(input("Enter key: "))
    val=(input("Enter value: "))
    dic[key]=val
    leng-=1
print(dic)
# create 2 list of equal len ,convert it two dict list1 as key and list2 as val

lis1=[]
lis2=[]

leng=int(input("Enter len of list: "))
leng2=leng
len3=leng
print("Enter element of list1")
while(leng>0):
    a=input("Element: ")
    lis1.append(a)
    leng-=1

print("Enter element of list2")
while(leng2>0):
    a=input("Element: ")
    lis2.append(a)
    leng2-=1

dic={}
i=0
while(len3>0):
    # key=(input("Enter key: "))
    # val=(input("Enter value: "))
    dic[lis1[i]]=lis2[i]
    i+=1
    len3-=1
print(dic)

