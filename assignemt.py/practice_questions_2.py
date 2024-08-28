#1
l=[1,2,3,4,5,6,7,8]
t=tuple(l[:5])
print(t)

#2
l=[1,2,3,4,5,6,7,8]
t=tuple(l[-5:])
print(t)

#3
l=[1,2,3,4,5,6,7,8]
n=len(l)
#1
print(l[::2])
#2
print(l[1:])
#3
if n==4:
    print(l)

#4
l=[i for i in range(0,96)]
#1
def mult_five(l):
    l2=list()
    for i in l:
        if i%5==0:
            l2.append(i)
    return l2
print(mult_five(l))
#2
l2=list()
for i in l:
    if i%4==0 and i%6==0:
        l2.append(i)
print(l2)
#3
l3=list()
for i in l:
    if i%13==0:
        l3.append(i)
print(l3)


