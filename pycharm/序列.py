s=[1,2,3,4,5]
print(id(s))
s*=2
print(s," ",id(s))

t=(1,2,3,4,5)
print(id(t))
t*=2
print(t," ",id(t))

x=[1,2,3]
y=[1,2,3]
print(x is y)
m="hallo world"
n="hallo world"
print(m is n)

# del x,y
# print(x,y)
del x[:]
print(x)

print(list("hallo world"))
print(tuple("hallo world"))
print(str([1,2,3,4,5,6]))
print(max([1,2,3,4,5,6])," ",min("halloworld"))
print(min([],default="空列表无法查询"))
print(sum([1,2,3,4,5]))

newList=[1,2,3,4,5]
print(sorted(newList) is newList)
print(sorted(newList,reverse=True))
newStr=["abjabgkab","ahgwys","y8qggbk","whn","qhgbkavhagsbgqa"]
print(sorted(newStr,key=len))
newStr.sort(key=len)
print(newStr)
print(list(reversed(range(0,10,2))))

newStr2=["abc","def","ghi","jkl"]
print(list(enumerate(newStr2)))
x=[1,2,3]
y=[4,5,6]
z=[7,8,9,10,11]
print(list(zip(x,y)))
import itertools
print(list(itertools.zip_longest(x,y,z)))
mapped=map(pow,[1,2,3],[4,5,6])
print(list(mapped))
print(list(mapped))
name="FishC"
print(list(filter(str.islower,name)))
it=iter(name)
while True:
    print(next(it))