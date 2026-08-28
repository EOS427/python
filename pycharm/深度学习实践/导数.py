

def numerical_diff(f,x):
    h=1e-50
    return (f(x+h)-f(x))/h

def numericial_diff_2(f,x):
    h=1e-4
    return (f(x+h)-f(x-h))/(2*h)

def func_1(x):
    return 0.01*x**2+0.1*x

import numpy as np
import matplotlib.pylab as plt
# x=np.arange(0.0,20.0,0.1)
# y=func_1(x)
# plt.xlabel("x")
# plt.ylabel("f(x)")
# plt.plot(x,y)
# # plt.show()
#
# print(numericial_diff_2(func_1,5))
# print(numericial_diff_2(func_1,10))
# k1=numericial_diff_2(func_1,5)
# k2=numericial_diff_2(func_1,10)

def linear_func(f,x):
    y=f(x)
    k=numericial_diff_2(f,x)
    def func_build(x2):
        return k*(x2-x)+y
    return func_build

# y2=linear_func(func_1,5)
# y3=linear_func(func_1,10)
# y22=y2(x)
# y32=y3(x)
# plt.plot(x,y22)
# plt.plot(x,y32)
# plt.show()

def square_x(tuple):
    return tuple[0]**2+tuple[1]**2

def fixed_first_variable(x0):
    return x0**2+4.0**2

def fixed_second_variable(x1):
    return 3.0**2+x1**2

# print(fixed_first_variable(3.0))
# print(fixed_second_variable(4.0))
# print(numericial_diff_2(fixed_first_variable,3.0))
# print(numericial_diff_2(fixed_second_variable,4.0))


def numerical_gradient(func,list):
    h=1e-4
    grad=np.zeros_like(list)
    for index in range(len(list)):
        cur_val=list[index]
        list[index]=cur_val+h
        subtractor=func(list)
        list[index]=cur_val-h
        minuend=func(list)
        grad[index]=(subtractor-minuend)/(2*h)
        list[index]=cur_val
    return grad

# print(numerical_gradient(square_x,np.array([4.0,3.0])))

def grad_decent(f,init_x,lr=0.1,time=100):
        x=init_x
        for it in range(time):
            cur_grad=numerical_gradient(f,x)
            x-=cur_grad*lr
        return x

# init_list=np.array([-3.0,4.0])
# print(grad_decent(f=square_x,init_x=init_list))

# import platform
# print(platform.architecture())
# exit()


import sys, os
sys.path.append(os.pardir)
import numpy as np
from common.functions import softmax, cross_entropy_error
from common.gradient import numerical_gradient

class simpleNet:

    def __init__(self):
        self.w=np.random.randn(2,3)

    def predict(self,x):
        return np.dot(x,self.w)

    def loss(self,x,t):
        z=self.predict(x)
        y=softmax(z)
        loss=cross_entropy_error(y,t)
        return loss

# net=simpleNet()
# print(net.w)
# x=np.array([0.6,0.9])
# p=net.predict(x)
# print(p)

# def f(w):
#     return net.loss(x, t)
# dw=numerical_diff(f,net.w)
# print(dw)

import sys, os
sys.path.append(os.pardir)
from common.functions import *
from common.gradient import numerical_gradient

class TwoLayerNet:

    def __init__(self,input_size,hidden_side,output_side,weight_init_str=0.01):
        self.params={}
        self.params['W1']=weight_init_str*np.random.randn(input_size,hidden_side)
        self.params['b1']=np.zeros(hidden_side)
        self.params['W2']=weight_init_str*np.random.randn(hidden_side,output_side)
        self.params['b2']=np.zeros(output_side)

    def prediction(self,x):
        W1,W2=self.params['W1'],self.params['W2']
        b1,b2=self.params['b1'],self.params['b2']
        a1=np.dot(x,W1)+b1
        z1=sigmoid(a1)
        a2=np.dot(z1,W2)+b2
        z2=softmax(a2)
        return z2

    def loss(self,x,t):
        y=self.prediction(x)
        return cross_entropy_error(y,t)

    def accuracy(self,x,t):
        y=self.prediction(x)
        y=np.argmax(y,axis=1)
        t=np.argmax(t,axis=1)
        return np.sum(y==t)/float(x.shape[0])

    def numerical_gradient(self,x,t):
            loss_W=lambda w:self.loss(x,t)
            grads = {}
            grads['W1'] = numerical_gradient(loss_W, self.params['W1'])
            grads['b1'] = numerical_gradient(loss_W, self.params['b1'])
            grads['W2'] = numerical_gradient(loss_W, self.params['W2'])
            grads['b2'] = numerical_gradient(loss_W, self.params['b2'])
            return grads


from dataset.mnist import load_mnist

(x_train, t_train), (x_test, t_test) = load_mnist(normalize=True, one_hot_label = True)

iters_num = 10000
train_size = x_train.shape[0]
batch_size = 100
learning_rate = 0.1
train_loss_list = []
train_acc_list = []
test_acc_list = []
# 平均每个epoch的重复次数
iter_per_epoch = max(train_size / batch_size, 1)
network = TwoLayerNet(input_size=784, hidden_side=50, output_side=10)
# print(x_train.shape)
# print(network.params['W1'].shape)

for i in range(iters_num):
# 获取mini-batch
    batch_mask = np.random.choice(train_size, batch_size)
    x_batch = x_train[batch_mask]
    t_batch = t_train[batch_mask]
# 计算梯度
    grad = network.numerical_gradient(x_batch, t_batch)
# grad = network.gradient(x_batch, t_batch) # 高速版!
# 更新参数
    for key in ('W1', 'b1', 'W2', 'b2'):
        network.params[key] -= learning_rate * grad[key]
        # 记录学习过程
        loss = network.loss(x_batch, t_batch)
        train_loss_list.append(loss)
    if i % iter_per_epoch == 0:
        train_acc = network.accuracy(x_train, t_train)
        test_acc = network.accuracy(x_test, t_test)
        train_acc_list.append(train_acc)
        test_acc_list.append(test_acc)
        print("train acc, test acc | " + str(train_acc) + ", " + str(test_acc))

