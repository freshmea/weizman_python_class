import tensorflow as tf
import numpy as np

#변수 생성

x=tf.Variable(20.0)
print(x)

x= tf.Variable(2.0)
y= tf.Variable(3.0)

with tf.GradientTape() as tape:
    y_sq= y**2
    z= x**2 +tf.stop_gradient(y_sq)

grad= tape.gradient(z, {'x':x, 'y':y})

print('dz/dx', grad['x'])
print('dz/dy', grad['y'])

def sigmoid(x):
    return (1/(1+np.exp(-x)))

def Neuron(x, W, bias=0):
    z= x*W + bias
    return sigmoid(z)

x= tf.random.normal((2,1), 0, 1)
W= tf.random.normal((2,1), 0, 1)

print(x.shape, x)
print(W.shape, W)

print(Neuron(x, W))

#가중치 구현

x=1
y=0
W=tf.random.normal([1], 0, 1)
print(Neuron(x,W))
print('y:', y)

for i in range(1000):
    output = Neuron(x, W)
    error=y-output
    W=W+x*0.1*error

    if i%100 ==99:
        print("{}\t{}\t{}".format(i+1, error, output))


def Neuron2(x, W, bias=0):
    z=tf.matmul(x, W, transpose_b=True)+bias
    return sigmoid(z)

x= tf.random.normal((1,3), 0, 1)
y= tf.ones(1)
W= tf.random.normal((1,3), 0, 1)

print(Neuron2(x, W))
print('y:', y)

for i in range(1000):
    output = Neuron2(x, W)
    error = y-output
    W=W+x*0.1*error

    if i%100 ==99:
        print("{}\t{}\t{}".format(i+1, error, output))
