print('"Hello\nWorld"')

# single line comment
"""
Multi
line 
comment
"""
"""
1. numbers, alpha, _
2. first char should not be a num
3. whitespace not allowed first_name
4. short and desc
5. no keywords

int 9
float 9.0
string ''
bool True False
complex 2+5j
binary bytes, memoryview, bytearray

m = 'hello'
n = 78
print("the value of m is"+m)
print(f"the value of n is {n}")

Arithmetic Operators - + - * / % //
Assignment Operators - = += -= *= /= %= //=
Comparison Operators - > < >= <= == != <>
Logical Operators - and or not
cond1 and cond2
T T = T
T F = F
F T = F
F F = F
cond1 or cond2
T T = T
T F = T
F T = T
F F = F
not(cond)
T = F
F = T
Bitwise Operators - >> <<
Identity Operator - is is not
Membership Operators - in not in

a = [7,8]
b = [7,8]
print(7 not in a)

import sys

print(sys.argv)

n = float(input("Enter a number"))
print(n+3)

simple if
if cond:
    True stat
if - else
if cond:
    True Stat
else:
    False stat
elif ladder
if cond1:
    T Stat
elif cond2:
    T stat
else:
    F Stat

place = "Manali"
if place == "Goa":
    print("Chalo Goa")
elif place == 'Manali':
    print('Manali')
elif place == 'Kerala':
    print('Kerala')
else:
    print(place)

place = 'Goa'
drink = True
if place == 'Goa':
   pass
else:
    if drink:
        print('Not going')
    else:
        print('Going')

for m in lst:
    print

while cond:
    print


lst = [34,89,10,20,40]
l = [1,2,3,4,5,6,7,8,9,10]
for m in lst:
    i = 1
    while i <= 10:
        print(i*m)
        i += 1
    print('************')

lst = [10,20,30,40,50]
for m in lst:
    if m == 30:
        continue
    print(m)

range(2000)stop
range(500,1000)start, stop
range(1,10,2) start, stop, step
1,2,3,4,5,6,7,8,9
1,3,5,7,9

n = list(range(10))
print(n)
for m in range(1,10,3):
    print(m**3)

s1 = '        heLLo     '
s2 = 'woRlD'
# s3 = s1+ ' ' + s2
# print(s1*2)
# for m in s1:
#     print(m)
# print('length',len(s1))
# print(s1[1::2])
# print(s1.upper())
# print(s1.lower())
# print(s3.title())
# print(s3.capitalize())
print(s1.strip()+s2)

s = 'hello,world'
print(s.split(','))
lst = ['a','b','c']
print(','.join(lst))
print(s.replace('world', 'python'))
print(s.find('python',4,11))
print(s.index('world'))
print(s.startswith('hello'))
print(s.endswith('world'))

lst = [10,20,30,40,50]
print(lst)
#print(lst[1:4])
lst.append(60)
print(lst)
lst.insert(2,70)
print(lst)
lst.extend([80,90,100])
print(lst)
lst[2] = 700
print(lst)
lst.pop()
print(lst)
lst.pop(2)
print(lst)
del lst[1]
print(lst)
lst.remove(60)
print(lst)
lst.clear()
print(lst)
del lst
print(lst)

lst = [45,89,10,56,20]
print(lst)
# print(sorted(lst, reverse=True))
# print(lst)
lst.reverse()
print(lst)
print(len(lst))
print(lst.count(10))
print(lst.index(10))
print(min(lst))
print(max(lst))
print(sum(lst))

lst1 = [1,2,3,4,5]
lst2 = [6,7,8,9]
print(lst1*2)
print(lst1+lst2)

t = (1,2,3,4,5)
print(t)

s = {10,20,30,70,10}
print(s)
s.add(60)
print(s)
s.update({50,90,40})
print(s)
s.pop()
print(s)
s.remove(10)
print(s)
s.discard(60)
print(s)
print(len(s))
s.clear()
print(s)
del s
print(s)

d1 = {'k1':'v1','k2':'v2','k3':'v3'}
print(d1)
d1.update({'k4':'v4','k5':'v5'})
print(d1)
print(d1.get('k4'))
# print(d1['k2'])
# d1['k2'] = 'v4'
# print(d1)
# d1['k4'] = 'v2'
# print(d1)
# d1.pop('k2')
# print(d1)
# del d1['k4']
# print(d1)
# d1.clear()
# print(d1)
# del d1
# print(d1)
for m, n in d1.items():
    print(m, '********', n)

for m in d1.keys():
    print(m)

for m in d1.values():
    print(m)

lst = []
for m in range(1,6):
    lst.append(m**3)
print(lst)

lst = [m**3 for m in range(1,6) if m%2==0]
print(lst)


d = {}
for m in range(1,6):
    d[m] = m**3
print(d)
"""
d = {m:m**3 for m in range(1,6) if m%2==0}
print(d)