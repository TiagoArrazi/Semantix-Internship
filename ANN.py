import tensorflow as tf
import numpy as np
import pandas as pd
from collections import Counter
from sklearn.datasets import fetch_20newsgroups

categories = ["comp.graphics", "sci.space", "rec.sport.baseball"]
newsgroups_train = fetch_20newsgroups(subset = 'train', categories = categories)
newsgroups_test = fetch_20newsgroups(subset = 'test', categories = categories)


vocab = Counter()

text = "Hi from Brazil"

#Get all words
for word in text.split(' '):
    word_lowercase = word.lower()
    vocab[word_lowercase] += 1

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




#Now we have an index
word2index = get_word_2_index(vocab)

total_words = len(vocab)

#This is how we create a numpy array (our matrix)
matrix = np.zeros((total_words), dtype = float)

#Now we fill the values
for word in text.split():
    matrix[word2index[word]] += 1



#Network parameters

n_hidden_1 = 10       #1st layer, number of features
n_hidden_2 = 5        #2nd layer, number of features
n_input = total_words #Words in vocab
n_classes = 3         #Categories: graphics, space and baseball

weights = {
            'h1': tf.Variable(tf.random_normal([n_input, n_hidden_1])),
            'h2': tf.Variable(tf.random_normal([n_hidden_1, n_hidden_2])),
            'out': tf.Variable(tf.random_normal([n_hidden_2, n_classes]))
          }

biases = {
            'b1': tf.Variables(tf.random_normal([n_hidden_1])),
            'b2': tf.Variables(tf.random_normal([n_hidden_2])),
            'out': tf.Variables(tf.random_normal([n_classes]))
         }

def multilayer_perceptron(input_tensor, weights, biases):
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


#Construct model
prediction = multilayer_perceptron(input_tensor, weights, biases)

#Define loss
entropy_loss = tf.nn.softmax_cross_entropy_with_logits(logits = prediction, labels = output_tensor)
loss = tf.reduce_mean(entropy_loss)

optimizer = tf.train.AdamOptimizer(learning_rate = learning_rate).minimize(loss)
