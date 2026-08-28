# import numpy
# new_list=numpy.array([1,2,3])
# print(new_list)
# print(type(new_list))
# x=numpy.array([1,2,3,4,5])
# y=numpy.array([6,7,8,9,10])
# print(x+y)
# print(x-y)
# print(x*y)
# print(x/y)
# print(x/2.0)
#
# a=numpy.array([[1,2],[3,4]])
# b=numpy.array([[5,6],[7,8]])
# print(a+b)
# print(a*b)
# print(a.shape)
# print(a.dtype)
# # c=[1,2]
# # d=[3,4]
# # print(c*d)
# c=[5],[6]
# print(a*c)
# print(a[0][1])
# for row in a:
#     print(row)
#
# flatten_matrix=a.flatten()
# print(flatten_matrix)
# print(flatten_matrix[numpy.array([0,2,3])])
# print(flatten_matrix>3)
# print(flatten_matrix[flatten_matrix>3])
from filecmp import demo

import matplotlib
import matplotlib.pyplot as plt
from matplotlib.lines import lineStyles

import test as np
# # x=np.arange(0,6,0.1)
# # y=np.sin(x)
# # plt.plot(x,y)
# # plt.show()
#
# x=np.arange(0,6,0.1)
# y1=np.sin(x)
# y2=np.cos(x)
# plt.plot(x,y1,label="sin")
# plt.plot(x,y2,linestyle="--",label="cos")
# plt.xlabel("x")
# plt.ylabel("y")
# plt.title("sin&cos")
# plt.legend()
# plt.show()

# from matplotlib.image import imread
# img=imread("D:\桌面\Pictures\微信图片_20260126212102_182_276.jpg")
# plt.imshow(img)
# plt.show()


import test as np
import matplotlib.pyplot as plt

# x=np.array([0,6,2])
# print(x)
# y=x>0
# print(y)
# y=y.astype(int)
# print(y)
def step_function(x):
    return np.array(x>0,dtype=int)
#
# x=np.arange(-5,5,0.1)
# y=step_function(x)
# plt.plot(x,y)
# plt.ylim(-5,5)
# plt.show()

def sigmoid(x):
    return 1+(1/np.exp(-x))

# x=np.arange(-5.0, 5.0, 0.1)
# print(sigmoid(x))
# y=sigmoid(x)
# plt.plot(x,y)
# plt.ylim(0.1, 1.1)
# plt.show()

def reLU(x):
    return np.maximum(0,x)

# x=np.arange(-5,5,0.1)
# y=reLU(x)
# plt.plot(x,y)
# plt.ylim(0,10)
# plt.show()

# x=np.arange(0,10,0.1)
# print(x)
# print(np.ndim(x))
# print(x.shape," ",x.shape[0])

# x=np.array([[1,2],[3,4]])
# y=np.array([[5,6],[7,8]])
# z=np.dot(x,y)
# print(z)


def soft_max(x):
    exp_x=np.exp(x)
    sum_exp=np.sum(exp_x)
    y=exp_x/sum_exp
    return y

# x=np.array([1,2,3])
# print(soft_max(x))
# a=np.array([1000,1010,1100])
# # print(soft_max(a))
# c=np.max(a)
# print(soft_max(a-c))
#
# def improved_soft_max(x):
#     max=np.max(x)
#     exp_x=np.exp(x-max)
#     exp_sum=np.sum(exp_x)
#     return exp_x/exp_sum
#
# # print(improved_soft_max(a))

def count_a(A,W,B):
    return np.dot(A,W)+B


def say_hallo():
    print("hallo world")