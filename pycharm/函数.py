def myFunc(first,second,third="I"):
    return " ".join((third,second,first))

print(myFunc("you","and"))
print(myFunc("you","and","me"))
print(myFunc("me",third="you",second="me"))

def abc(a,/,b,c):
    return a+b+c
print(abc(1,2,3))
print(abc(1,b=3,c=4))

def bcd(a,*,b,c):
    print(a+b+c)

bcd(1,b=2,c=3)

def efg(*args):
    print("第2个参数是{}".format(args[1]))
def fgh(*args,a,b):
    print("第{}个参数与第{}个参数之和为{}".format(a,b,args[a-1]+args[b-1]))
def hij(**kwds):
    print(kwds)
def jkl(a,*b,**kwds):
    print(a,b,kwds)
fgh(1,2,3,4,5,a=1,b=4)
efg(1,2,3,4)
hij(a=1,b=2,c=3,d=4)
jkl(1,2,3,4,5,x=6,b=7,c=8,d=9)

x=(1,2,3,4)
y={"a":1,"b":2,"c":3,"d":4}
def newFunc(a,b,c,d):
    print(a,b,c,d)
efg(*x)
hij(**y)
newFunc(*x)
newFunc(*y)
newFunc(**y)

matrix=[[1,2,3],[4,5,6],[7,8,9]]
first,second,third=zip(*matrix)
print(first)
print(second)
print(third)