import sys, os
sys.path.append(os.pardir)
import numpy as np
import pickle
from PIL import Image
from common.functions import *
from dataset.mnist import load_mnist



def img_show(img):
    pil_img = Image.fromarray(np.uint8(img))
    pil_img.show()

(x_train, t_train), (x_test, t_test) = load_mnist(flatten=True,
normalize=False)
img = x_train[0]
label = t_train[0]
print(label) # 5

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
    with open("../deep-learning-from-scratch-master/deep-learning-from-scratch-master/ch03/sample_weight.pkl", 'rb') as f:# 以二进制读取模式打开文件
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

x, t = get_data()
network = init_network()
accuracy_cnt = 0
for i in range(len(x)):
    y = predict(network, x[i])
    p = np.argmax(y) # 获取概率最高的元素的索引
    if p == t[i]:
        accuracy_cnt += 1
print("Accuracy:" + str(float(accuracy_cnt) / len(x)))