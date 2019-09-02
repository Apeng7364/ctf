import tensorflow as tf
import numpy as np
from math import isclose
from scipy.special import logit
np.set_printoptions(precision=20)
np.set_printoptions(threshold='nan')

def judge(a, b):
    for i in range(32):
        m = a[i]
        n = b[i]
        print(m, n)
        #if not isclose(m, n, rel_tol=1e-8):
        #    return i
    return 32

def trans(secret):
    return np.array([float(ord(x))/128 for x in secret])
def tran(b):
    return np.array([x for x in b])

fakeflag = "flag{01234567012345670123456789}"
X = trans(fakeflag)
#print(X)
sess = tf.Session()
saver = tf.train.import_meta_graph('model.meta')
saver.restore(sess, tf.train.latest_checkpoint('./'))
graph = tf.get_default_graph()
x = graph.get_tensor_by_name('In_string:0')
y = graph.get_tensor_by_name("Out_judge:0")
final = np.array([[1.40895243e-01, 9.98096014e-01, 1.13422030e-02, 6.57041353e-01,
    9.97613889e-01, 9.98909625e-01, 9.92840464e-01, 9.90108787e-01,
    1.43269835e-03, 9.89027450e-01, 7.22652880e-01, 9.63670217e-01,
    6.89424259e-01, 1.76012035e-02, 9.30893743e-01, 8.61464445e-03,
    4.35839722e-01, 8.38741174e-04, 6.38429400e-02, 9.90384032e-01,
    1.09806946e-03, 1.76375112e-03, 9.37186997e-01, 8.32329340e-01,
    9.83474966e-01, 8.79308946e-01, 6.59324698e-03, 7.85916088e-05,
    2.94269115e-05, 1.97006621e-03, 9.99416387e-01, 9.99997202e-01]])

res = sess.run(y, feed_dict={x:[X]})
#print(res[0])

def gn(nm):
    a=graph.get_tensor_by_name(nm + ":0")
    return sess.run(a, feed_dict={x:[X]})

def gv(v):
    return sess.run(v, feed_dict={x:[X]})



In_string = gn("In_string")
v0 = gn("Variable/read")
v1 = gn("Variable_1/read")
v2 = gn("Variable_2/read")
v3 = gn("Variable_3/read")
v4 = gn("Variable_4/read")
v5 = gn("Variable_5/read")
temp=gn("PRECISEFINAL")

def invsigmoid(a):
    b= np.array([[0.0]*32])
    for i in range(32):
        b[0][i]=logit(a[0][i])
    return b

a = np.array([[1.40895243e-01, 9.98096014e-01, 1.13422030e-02, 6.57041353e-01,
    9.97613889e-01, 9.98909625e-01, 9.92840464e-01, 9.90108787e-01,
    1.43269835e-03, 9.89027450e-01, 7.22652880e-01, 9.63670217e-01,
    6.89424259e-01, 1.76012035e-02, 9.30893743e-01, 8.61464445e-03,
    4.35839722e-01, 8.38741174e-04, 6.38429400e-02, 9.90384032e-01,
    1.09806946e-03, 1.76375112e-03, 9.37186997e-01, 8.32329340e-01,
    9.83474966e-01, 8.79308946e-01, 6.59324698e-03, 7.85916088e-05,
    2.94269115e-05, 1.97006621e-03, 9.99416387e-01, 9.99997202e-01]])



a0=invsigmoid(res)
a1=tf.subtract(a0,v5)
a2=tf.matmul(a1,tf.matrix_inverse(v2))
a3=tf.atanh(a2)
a4=tf.subtract(a3,v4)
a5=tf.matmul(a4,tf.matrix_inverse(v1))
a6=invsigmoid(gv(a5))
a7=tf.subtract(a6,v3)
a8=tf.matmul(a7,tf.matrix_inverse(v0))
l=gv(a8).tolist()
ll=l[0]
flag=''
for i in range(len(ll)):
    ll[i]*=128
    ll[i]=round(ll[i])
    flag+=chr(ll[i])
print(flag)


'''

t0 = tf.matmul(In_string, v0)
t1 = tf.add(t0, v3)
t2 = tf.sigmoid(t1)
t3 = tf.matmul(t2, v1)
t4 = tf.add(t3, v4)
t5 = tf.tanh(t4)
t6 = tf.matmul(t5, v2)
t7 = tf.add(t6, v5)
t8 = tf.sigmoid(t7)
print(gv(t8))
'''


'''
sess = tf.Session()
saver = tf.train.import_meta_graph('model.meta')
saver.restore(sess, tf.train.latest_checkpoint('./'))
graph = tf.get_default_graph()
tf.train.write_graph(graph, './aaa', 'train.pbtxt')
'''