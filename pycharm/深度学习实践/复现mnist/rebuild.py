import sys, os
import matplotlib.pylab as plt
base = os.path.dirname(os.path.abspath(__file__))
repo = os.path.join(base, "..", "deep-learning-from-scratch-master",
                    "deep-learning-from-scratch-master")
# sys.path.append(os.pardir)
sys.path.append(repo)
import numpy as np
import pickle
from PIL import Image
from common.functions import *
from dataset.mnist import load_mnist



def img_show(img):
    pil_img = Image.fromarray(np.uint8(img))
    pil_img.show()

# (x_train, t_train), (x_test, t_test) = load_mnist(flatten=True,
# normalize=False)
# img = x_train[0]
# label = t_train[0]
# print(label) # 5
# print(img.shape) # (784,)
# img = img.reshape(28, 28) # 把图像的形状变成原来的尺寸
# print(img.shape) # (28, 28)
#
# img_show(img)


def get_data():
    (x_train, t_train), (x_test, t_test) = \
    load_mnist(normalize=True, flatten=True, one_hot_label=False)
    return x_test, t_test

def init_network():
    with open(os.path.join(repo, "ch03", "sample_weight.pkl"), 'rb') as f:# 以二进制读取模式打开文件
          network = pickle.load(f)#序列化，返回字典
    return network

def predict(network, x):
    W1, W2, W3 = network['W1'], network['W2'], network['W3']
    b1, b2, b3 = network['b1'], network['b2'], network['b3']
    a1 = np.dot(x, W1) + b1
    z1 = sigmoid(a1)
    a2 = np.dot(z1, W2) + b2
    z2 = sigmoid(a2)
    a3 = np.dot(z2, W3) + b3
    y = softmax(a3)
    return y

# x, t = get_data()
# network = init_network()
# accuracy_cnt = 0
# for i in range(len(x)):
#     y = predict(network, x[i])
#     p = np.argmax(y) # 获取概率最高的元素的索引
#     if p == t[i]:
#         accuracy_cnt += 1
# print("Accuracy:" + str(float(accuracy_cnt) / len(x)))

# x, t = get_data()
# network = init_network()
# batch_size = 100 # 批数量
# accuracy_cnt = 0
# for i in range(0, len(x), batch_size):
#     x_batch = x[i:i+batch_size]
#     y_batch = predict(network, x_batch)
#     p = np.argmax(y_batch, axis=1)
#     accuracy_cnt += np.sum(p == t[i:i+batch_size])
# print("Accuracy:" + str(float(accuracy_cnt) / len(x)))

def cross_entropy_error(y, t):
    delta = 1e-7
    return -np.sum(t * np.log(y + delta))

#mini_batch
(x_train, t_train), (x_test, t_test) = \
load_mnist(normalize=True, one_hot_label=True)
print(x_train.shape) # (60000, 784)
print(t_train.shape) # (60000, 10)

train_size = x_train.shape[0]
batch_size = 10
batch_mask = np.random.choice(train_size, batch_size)
x_batch = x_train[batch_mask]
t_batch = t_train[batch_mask]

def new_cross_entropy_error(y, t):
    if y.ndim == 1:
        t = t.reshape(1, t.size)
        y = y.reshape(1, y.size)
    batch_size = y.shape[0]
    return -np.sum(t * np.log(y + 1e-7)) / batch_size

def numerical_diff(f, x):#中心差分，拉格朗日中值定理
    h = 1e-4 # 0.0001
    return (f(x+h) - f(x-h)) / (2*h)

# def function_1(x):
#     return 0.01*x**2 + 0.1*x
# x = np.arange(0.0, 20.0, 0.1) # 以0.1为单位，从0到20的数组x
# y = function_1(x)
# plt.xlabel("x")
# plt.ylabel("f(x)")
# plt.plot(x, y)
# plt.show()

def numerical_gradient(f, x):
    h = 1e-4 # 0.0001
    grad = np.zeros_like(x) # 生成和x形状相同的数组
    for idx in range(x.size):
        tmp_val = x[idx]
        # f(x+h)的计算
        x[idx] = tmp_val + h
        fxh1 = f(x)
        # f(x-h)的计算
        x[idx] = tmp_val - h
        fxh2 = f(x)
        grad[idx] = (fxh1 - fxh2) / (2*h)
        x[idx] = tmp_val # 还原值
    return grad

def gradient_descent(f, init_x, lr=0.01, step_num=100):
    x = init_x
    for i in range(step_num):
        grad = numerical_gradient(f, x)
        x -= lr * grad
    return x