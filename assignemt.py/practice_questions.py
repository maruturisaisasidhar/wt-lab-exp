list_a = [1,2,36.7,0.9,'1',9,27,31,0,1.1,34,2,3.4,7,3,2]

#1
s=0
for i in list_a:
    if type(i) is int or type(i) is float:
        s+=i
print('sum is',s)

#2
#variation1
max=list_a[0]
for i in list_a:
    if type(i) is int or type(i) is float:
        if i>max:
            max=i
print('Maximum element using first element is',max)
#variation2
max=list_a[-1]
for i in list_a:
    if type(i) is int or type(i) is float:
        if i>max:
            max=i
print('Maximum element using last element is',max)

#3
for ind,item in enumerate(list_a):
    if item=='1':
        print("Index of '1' is",ind)
        break

#4
ints=[]
floats=[]
strs=[]
other_dtypes=[]
for i in list_a:
    if type(i) is int:
        ints.append(i)
    elif type(i) is float:
        floats.append(i)
    elif type(i) is str:
        strs.append(i)
    else:
        other_dtypes.append(i)
print("ints",ints)
print("float",floats)
print("string",strs)


#5
set_a=set(list_a)
print('Duplicates are:')
for i in set_a:
    if list_a.count(i)>1:
        print(i)
print('Non Duplicate elements are')
for i in set_a:
    if list_a.count(i)==1:
        print(i)
        
d=dict()
for i in set_a:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
print('The frequency of each element is',d)