
import numpy as np
import tensorflow as tf



n_input = 7
n_hidden = 2
n_output = 7

stepshow = 1000

#input for single file array needs to be recreated for everytime
x_raw = np.array([[4,2,3,8,7,84,4]])
y_raw = np.array([0,0,0,0,0,1,0])
y_raw = np.reshape(y_raw,(1,n_output))

W = { "h1": tf.Variable(tf.ones([n_input, n_hidden]),name="h1"),
        "out": tf.Variable(tf.ones([n_hidden, n_output]))
}

b = { "b1": tf.Variable(tf.zeros([n_hidden])),
        "bout": tf.Variable(tf.zeros([n_output]))
}

x = tf.placeholder("float", [None, n_input])
y = tf.placeholder("float", [None, n_output])


l1 = tf.add(tf.matmul(x,W["h1"]),b["b1"])
l1_act = tf.sigmoid(l1)

out = tf.add(tf.matmul(l1_act,W["out"]),b["bout"])
out_act = tf.sigmoid(out)

cost = tf.reduce_mean(tf.abs(tf.subtract(out_act,y)))
train_step = tf.train.AdadeltaOptimizer(learning_rate=1.0).minimize(cost)



with tf.Session() as sess:
        sess.run(tf.global_variables_initializer())

        pred = out_act.eval({x: x_raw})
        print(pred)
        for epoch in range(9000):
            k = sess.run(train_step,feed_dict={x: x_raw,y: y_raw})
            if epoch% stepshow == 0:
                pred = out_act.eval({x: x_raw})
                print(pred)
        pred = out_act.eval({x: x_raw})
        print(pred)
