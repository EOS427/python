# import sys
# import os
#
# sys.path.append(os.pardir)
#
# from dataset.mnist import load_mnist
#
# (x_train,t_train),(x_test,t_test)=load_mnist()
#
# print(x_train.shape)
# print(t_train.shape)
# print(x_test.shape)
# print(t_test.shape)

# import sys,os
# sys.path.append(os.pardir)
# from dataset.mnist import load_mnist
# (x_train, t_train), (x_test, t_test) = load_mnist(flatten=True,normalize=False)
# print(x_train.shape)
# print(t_train.shape) # (60000,)
# print(x_test.shape) # (10000, 784)
# print(t_test.shape) # (10000,)

# import sys, os
# sys.path.append(os.pardir)
# import numpy as np
# from dataset.mnist import load_mnist
# from PIL import Image
# def img_show(img):
#      pil_img = Image.fromarray(np.uint8(img))
#      pil_img.show()
# (x_train, t_train), (x_test, t_test) = load_mnist(flatten=True,normalize=False)
# img = x_train[0]
# label = t_train[0]
# print(label) # 5
# print(img.shape) # (784,)
# img = img.reshape(28, 28) # 把图像的形状变成原来的尺寸
# print(img.shape) # (28, 28)
# img_show(img)

import pickle
import sys, os
sys.path.append(os.pardir)
import numpy as np
from dataset.mnist import load_mnist
from PIL import Image
#
# def img_show(img):
#     image=Image.fromarray(np.uint8(img))
#     image.show()
#
# (x_train,t_train),(x_test,t_test)=load_mnist(flatten=True,normalize=False)
#
# img=x_train[0]
# label=t_train[0]
# print(label)
# print(img.shape)
# img=img.reshape(28,28)
# print(img.shape)
# img_show(img)

def sigmoid(x):
    return 1/(1+np.exp(-x))

def soft_max(x):
    x_max=np.max(x)
    exp_x=np.exp(x-x_max)
    exp_sum=np.sum(exp_x)
    return exp_x/exp_sum

def get_data():
    (x_train,t_train),(x_test,t_test)=load_mnist(flatten=True,normalize=True,one_hot_label=False)
    return x_test,t_test

def init_network():
    with open("sample_weight.pkl", 'rb') as file:
        network=pickle.load(file)
    return network

def predict(network,x):
    w1,w2,w3=network['W1'],network['W2'],network['W3']
    b1,b2,b3=network['b1'],network['b2'],network['b3']
    a1=np.dot(x,w1)+b1
    z1=sigmoid(a1)
    a2=np.dot(z1,w2)+b2
    z2=sigmoid(a2)
    a3=np.dot(z2,w3)+b3
    z3=soft_max(a3)
    return z3

# x,t=get_data()
# network=init_network()
# accuracy=0
# for num in range(len(x)):
#     probability_list=predict(network,x[num])
#     max_index=np.argmax(probability_list)
#     if max_index==t[num]:
#         accuracy+=1
# print(accuracy/len(x))

# batch_size=100
# for it in range(0,len(x),batch_size):
#     x_batch=x[it:it+batch_size]
#     y=predict(network,x_batch)
#     max=np.argmax(y,axis=1)
#     correct_result=t[it:it+batch_size]
#     print(np.sum(max==correct_result)/len(correct_result))

def mean_square_error(y,t):
    return 0.5*np.sum((y-t)**2)

# t = [0, 0, 1, 0, 0, 0, 0, 0, 0, 0]
# y = [0.1, 0.05, 0.6, 0.0, 0.05, 0.1, 0.0, 0.1, 0.0, 0.0]
#
# print(mean_square_error(np.array(y),np.array(t)))
# z = [0.1, 0.05, 0.1, 0.0, 0.05, 0.1, 0.0, 0.6, 0.0, 0.0]
# print(mean_square_error(np.array(z),np.array(t)))

def cross_entropy_error(y,t):
    min_num=1e-7
    return -np.sum(t*(np.log(y+min_num)))
#
# t = [0, 0, 1, 0, 0, 0, 0, 0, 0, 0]
# y = [0.1, 0.05, 0.6, 0.0, 0.05, 0.1, 0.0, 0.1, 0.0, 0.0]
# print(cross_entropy_error(np.array(y),np.array(t)))
# y = [0.1, 0.05, 0.1, 0.0, 0.05, 0.1, 0.0, 0.6, 0.0, 0.0]
# print(cross_entropy_error(np.array(y),np.array(t)))

import sys,os
sys.path.append(os.pardir)
import numpy as np
from dataset.mnist import load_mnist

(x_train,t_train),(x_text,t_test)=load_mnist(flatten=True,one_hot_label=True)
# print(x_train.shape)
# print(t_train.shape)
# train_size=x_train.shape[0]
# batch_size=10
# index_list=np.random.choice(train_size,batch_size)
# x_batch=x_train[index_list]
# t_batch=t_train[index_list]
# print(x_batch)
# print(t_batch)

def batch_CEE(y,t):
    if y.ndim==1:
        t.reshape(1,t.shape[0])
        y.reshape(1,y.shape[0])
    batch_num=y.shape[0]
    return -np.sum(t*np.log(y+1e-7))/batch_num

def special_CEE(y,t):
    if y.ndim==1:
        t.reshape(1,t.shape[0])
        y.reshape(1,y.shape[0])
    batch_num=y.shape[0]
    return 