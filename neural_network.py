import tensorflow as tf


#instansiate embeddigs
embeddings = tf.Variable(tf.random_uniform([vocabulary_size, embedding_size], -1.0, 1.0))



nce_weights = tf.Variable(tf.truncated_normal([vocabulary_size, embedding_size], stddev=1.0 / math.sqrt(embedding_size)))

#output weights
nce_biases = tf.Variable(tf.zeros([vocabulary_size]))
