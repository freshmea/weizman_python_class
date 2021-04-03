import tensorflow as tf
import numpy as np

a= tf.constant(2)
print(tf.rank(a))
print(a)

b=tf.constant([2,3])
print(tf.rank(b))
print(b)

c=tf.constant([[2,3], [6,7]])
print(tf.rank(c))
print(c)

d= tf.constant(['hello'])
print(tf.rank(d))
print(d)

rand = tf.random.uniform([1], 0, 1)
print(rand.shape)
print(rand)

rand2= tf.random.normal([1,2], 0, 1)
print(rand2.shape)
print(rand2)

rand3= tf.random.normal(shape=(3,2), mean=0, stddev=1)
print(rand3.shape)
print(rand3)

a= tf.constant(3)
b= tf.constant(2)
print(tf.add(a,b))
print(a+b)

c=tf.add(a,b).numpy()
print(type(c))

c_square = np.square(c, dtype = np.float32)
c_tensor = tf.convert_to_tensor(c_square)

print(c_tensor)
print(type(c_tensor))

t=tf.constant([[1., 2., 3.],[4., 5., 6.]])

print(t.shape)
print(t.dtype)

print(t[:,1:])
print(t[...,1,tf.newaxis])

print(t+10)
print(tf.square(t))
print(t @ tf.transpose(t))

#타입 변환시 tf. cast 사용

a= tf.constant(2)
print(a)

b= tf.constant(2.)
print(b)

#tf.constant(2.)+tf.constant(40) 타입에러

#tf.constant(2.)+tf.constant(30., dtype=tf.float64) 타입에러

t= tf.constant(30., dtype=tf.float64)
t2= tf.constant(4.)

print(t2+tf.cast(t, tf.float32))

#오토그래프 사용하기
import timeit
@tf.function
def my_function(x):
    return x**2-10*x+3

print(my_function(2))
print(my_function(tf.constant(2)))

def my_function_(x):
    return x**2-10*x+3

print(my_function_(2))
print(my_function_(tf.constant(2)))

tf_my_fuc=tf.function(my_function_)
print(tf_my_fuc)
print(tf_my_fuc(2))

def function_to_get_faster(x, y, b):
    x=tf.matmul(x,y)
    x=x+b
    return x

a_function_that_users_a_graph= tf.function(function_to_get_faster)

x1=tf.constant([[1.0, 2.0]])
y1=tf.constant([[2.0], [3.0]])
b1=tf.constant(4.0)

print(a_function_that_users_a_graph(x1, y1, b1).numpy())

def inner_function(x, y, b):
    x=tf.matmul(x,y)
    x=x+b
    return x

@tf.function
def outer_fuction(x):
    y=tf.constant([[2.0], [3.0]])
    b=tf.constant(4.0)
    return inner_function(x, y, b)

print(outer_fuction(tf.constant([[1.0, 2.0]])).numpy())

print(tf.autograph.to_code(my_function.python_function))

class SequentialModel(tf.keras.Model):
    def __init__(self, **kwargs):
        super(SequentialModel, self).__init__(**kwargs)
        self.flatten=tf.keras.layers.Flatten(input_shape=(28, 28))
        self.dense_1=tf.keras.layers.Dense(128, activation='relu')
        self.dropout = tf.keras.layers.Dropout(0.2)
        self.dense_2 = tf.keras.layers.Dense(10)

    def call(self, x):
        x=self.flatten(x)
        x=self.dense_1(x)
        x= self.dropout(x)
        x=self.dense_2(x)
        return x

input_data = tf.random.uniform([60, 28, 28])

eager_model = SequentialModel()
graph_model = tf.function(eager_model)

print('Eager time:', timeit.timeit(lambda : eager_model(input_data), number=10000))
print('Graph time:', timeit.timeit(lambda : graph_model(input_data), number=10000))


