#1
l=[1,2,3,4,5,6]
r=int(input())
n=len(l)
r=r%n
l[:n-r].reverse()
l[n-r:].reverse()
l.reverse()
print(l)

#2
first=second=-1
for num in l:
    if num > first:
        second = first
        first = num
    elif first > num > second:
        second = num
print(first,second)

#3
l1=[1,2,4,5,6,7]
l2=[1,3,4,5,6,9]
l3=[]
i=j=0
while(i<len(l1) and j<len(l2)):
    if l1[i]<l2[j]:
        l3.append(l1[i])
        i+=1
    else:
        l3.append(l2[j])
        j+=1
l3.extend(l1[i:])
l3.extend(l2[j:])

#4
j = 1
s = set(l[:1])
for i in range(1, n):
    if l[i] not in s:
        s.add(l[i])
        l[j] = l[i]
        j += 1
l = l[:j]
print(l)

#5
d=dict()
for i in l:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
print(d)

#6
l4=[]
for i in l1:
    if i in l2:
        l4.append(i)
print(l4)

#7
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 2, 'c': 4, 'd': 3}
dict3=dict()
for i,j in dict1.items():
    if dict2[i]==j:
        dict3[i]=j
print(dict3)

#8
def flatten(nl,l5):
    for i in nl:
        if isinstance(i,list):
            flatten(i,l5)
        else:
            l5.append(i)
nl=[1,2,[3,4,5,[6,7],8,9],10,11,[12]]
l5=list()

#9
l6=[1,-2,-3,-4,5,6,7,-8,9,-11]
pl=[]
nl=[]
for i in l6:
    if i<0:
        nl.append(i)
    else:
        pl.append(i)
print(pl,nl)
