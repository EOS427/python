# class C:
#     x=100
#     def set_x(self,new_x):
#         x=new_x
#
# c=C()
# c.set_x(200)
# print(c.x)
# C.x=300
# print(c.x)

class C:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2

    def sum(self):
        return self.num1+self.num2

    def minus(self):
        return self.num1-self.num2

c=C(1,2)
print(c.sum())
print(c.minus())

class A:
    def __init__(self,num):
        self.__num=num

    def get_num(self):
        return self.__num

a=A(5)
print(a.get_num())
print(a._A__num)
print(a.__dict__)
a.num2=10
print(a.__dict__)
a.__dict__["num3"]=15
print(a.__dict__)

class B:
    __slots__=("num","num2")
    def __init__(self,num,num2):
        self.num=num
        self.num2=num2

b=B(3,4)
print(b.num)
print(b.num2)
# b.num3=100


class myclass(str):
    def __new__(cls,string):
        string=string.upper()
        return super().__new__(cls,string)

    def __del__(self):
        print("deleted")

newclass=myclass("hallo world")
print(newclass)
# newnewclass=newclass
# del newclass
# del newnewclass
