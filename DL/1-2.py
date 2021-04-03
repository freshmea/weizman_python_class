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