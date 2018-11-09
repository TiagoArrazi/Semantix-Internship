import tensorflow as tf
import numpy as np
import pandas as pd
from collections import Counter
from sklearn.datasets import fetch_20newsgroups

categories = ["comp.graphics", "sci.space", "rec.sport.baseball"]
newsgroups_train = fetch_20newsgroups(subset = 'train', categories = categories)
newsgroups_test = fetch_20newsgroups(subset = 'test', categories = categories)

vocab = Counter()

#Get all words
for text in newsgroups_train.data:
    for word in text.split(' '):
        vocab[word.lower()] += 1

for text in newsgroups_test.data:
    for word in text.split(' '):
        vocab[word.lower()] += 1

#Convert words to indexes
def get_word_2_index(vocab):
    word2index = {}
    for i,word in enumerate(vocab):
        word2index[word] = i

    return word2index


def text_to_vector(text):
    layer = np.zeros(total_words, dtype = float)
    for word in text.split(' '):
        layer[word2index[word.lower()]] += 1

    return layer


def category_to_vector(category):
    y = np.zeros((3), dtype = float)
    if category == 0:
        y[0] = 1.
    elif category == 1:
        y[1] = 1.
    else:
        y[2] = 1.

    return y


def getBatch(df, i, batch_size):
    batches = []
    results = []
    texts = df.data[i * batch_size : i * batch_size + batch_size]
    categories = df.target[i * batch_size : i * batch_size + batch_size]

    for text in texts:
        layer = text_to_vector(text)
        batches.append(layer)
        
    for category in categories:
        y = category_to_vector(category)
        results.append(y)

    return np.array(batches), np.array(results)


#Now we have an index
word2index = get_word_2_index(vocab)

total_words = len(vocab)

#This is how we create a numpy array (our matrix)
matrix = np.zeros((total_words), dtype = float)

#Parameters
learning_rate = 0.01
training_epochs = 20
batch_size = 150
display_step = 1

#Network parameters
n_hidden_1 = 10       #1st layer, number of features
n_hidden_2 = 5        #2nd layer, number of features
n_input = total_words #Words in vocab
n_classes = 3         #Categories: graphics, space and baseball

input_tensor = tf.placeholder(tf.float32, [None, n_input], name = "input")
output_tensor = tf.placeholder(tf.float32, [None, n_classes], name = "output")

def multilayer_perceptron(input_layer, weights, biases):
    layer_1_multiplication = tf.matmul(input_tensor, weights['h1'])
    layer_1_addition = tf.add(layer_1_multiplication, biases['b1'])
    layer_1_activation = tf.nn.relu(layer_1_addition)

    #Hidden layer with RELU activation
    layer_2_multiplication = tf.matmul(layer_1_activation, weights['h2'])
    layer_2_addition = tf.add(layer_2_multiplication, biases['b2'])
    layer_2_activation = tf.nn.relu(layer_2_addition)

    #Output layer with linear activation
    out_layer_multiplication = tf.matmul(layer_2_activation, weights['out'])
    out_layer_addition = out_layer_multiplication + biases['out']
    
    return out_layer_addition

#Store layers weight and bias
weights = {
            'h1': tf.Variable(tf.random_normal([n_input, n_hidden_1])),
            'h2': tf.Variable(tf.random_normal([n_hidden_1, n_hidden_2])),
            'out': tf.Variable(tf.random_normal([n_hidden_2, n_classes]))
          }

biases = {
            'b1': tf.Variable(tf.random_normal([n_hidden_1])),
            'b2': tf.Variable(tf.random_normal([n_hidden_2])),
            'out': tf.Variable(tf.random_normal([n_classes]))
         }


#Construct model
prediction = multilayer_perceptron(input_tensor, weights, biases)

#Define loss and optimizer
entropy_loss = tf.nn.softmax_cross_entropy_with_logits_v2(logits = prediction, labels = output_tensor)

loss = tf.reduce_mean(entropy_loss)
optimizer = tf.train.AdamOptimizer(learning_rate = learning_rate).minimize(loss)

#Initializing the variables
init = tf.global_variables_initializer()

#[NEW] Add ops to save and restore all variables
saver = tf.train.Saver()

#Launch the graph
with tf.Session() as sess:
    sess.run(init)

    #Training cycle
    for epoch in range(training_epochs):
        avg_cost = 0
        total_batch = int(len(newsgroups_train.data) / batch_size)
        #Loop over all batches
        for i in range(total_batch):
            batch_x,batch_y = getBatch(newsgroups_train, i, batch_size)
            #Run optimization op (backdrop) and cost op (to get loss value)
            c,_ = sess.run([loss, optimizer], feed_dict = {input_tensor: batch_x, output_tensor: batch_y})
            #Compute average loss
            avg_cost += c / total_batch
        #Display logs per epoch step
        if epoch % display_step == 0:
            print("Epoch:", '%04d' % (epoch+1), "loss=", \
                "{:.9f}".format(avg_cost))

    print("Optimization Finished!")


# Test model
    correct_prediction = tf.equal(tf.argmax(prediction, 1), tf.argmax(output_tensor, 1))
    # Calculate accuracy
    accuracy = tf.reduce_mean(tf.cast(correct_prediction, "float"))
    total_test_data = len(newsgroups_test.target)
    batch_x_test,batch_y_test = getBatch(newsgroups_test,0,total_test_data)
    print("Accuracy:", accuracy.eval({input_tensor: batch_x_test, output_tensor: batch_y_test}))
    
    # [NEW] Save the variables to disk
    save_path = saver.save(sess, "/tmp/model.ckpt")
    print("Model saved in path: %s" % save_path)
