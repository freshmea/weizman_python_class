import tensorflow as tf
import numpy as np


키=[170, 180, 175, 160]
신발=[260, 270, 265, 280]
ss=0


a=tf.Variable(0.1)
b=tf.Variable(0.2)

def 손실함수():
    global ss
    if ss==3:
        ss=0
    ss+=1
    예측값 = 키[ss] * a + b
    return tf.square(신발[ss] - 예측값)

opt=tf.keras.optimizers.Adam(learning_rate=0.1)

for i in range(300):
    opt.minimize(손실함수,var_list=[a,b])
    print(a.numpy(), b.numpy())

print(170*a.numpy()+b.numpy())