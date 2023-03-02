import tensorflow as tf
from tensorflow.keras import layers

with tf.device('GPU:0'):
    layer1 = layers.Dense(16, input_dim=8)

with tf.device('GPU:1'):
    layer2 = layers.Dense(4, input_dim=16)
