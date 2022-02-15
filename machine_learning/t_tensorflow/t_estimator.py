import os
import time
#!pip install -q -U tensorflow-gpu
import tensorflow as tf
import numpy as np


(train_images, train_labels), (test_images, test_labels)= tf.keras.datasets.fashion_mnist.load_data()

TRAINING_SIZE = len(train_images)
TEST_SIZE = len(test_images)
train_images = np.asarray(train_images, dtype=np.float32) / 255
# Convert the train images and add channels
train_images = train_images.reshape((TRAINING_SIZE, 28, 28, 1))
test_images = np.asarray(test_images, dtype=np.float32) / 255
# Convert the test images and add channels
test_images = test_images.reshape((TEST_SIZE, 28, 28, 1))



# How many categories we are predicting from (0-9)
LABEL_DIMENSIONS = 10
train_labels = tf.keras.utils.to_categorical(train_labels,
                                             LABEL_DIMENSIONS)
test_labels = tf.keras.utils.to_categorical(test_labels,
                                            LABEL_DIMENSIONS)
# Cast the labels to floats, needed later
train_labels = train_labels.astype(np.float32)
test_labels = test_labels.astype(np.float32)


inputs = tf.keras.Input(shape=(28,28,1))  # Returns a placeholder
x = tf.keras.layers.Conv2D(filters=32,
                           kernel_size=(3, 3),
                           activation=tf.nn.relu)(inputs)
x = tf.keras.layers.MaxPooling2D(pool_size=(2, 2), strides=2)(x)
x = tf.keras.layers.Conv2D(filters=64,
                           kernel_size=(3, 3),
                           activation=tf.nn.relu)(x)
x = tf.keras.layers.MaxPooling2D(pool_size=(2, 2), strides=2)(x)
x = tf.keras.layers.Conv2D(filters=64,
                           kernel_size=(3, 3),
                           activation=tf.nn.relu)(x)
x = tf.keras.layers.Flatten()(x)
x = tf.keras.layers.Dense(64, activation=tf.nn.relu)(x)
predictions = tf.keras.layers.Dense(LABEL_DIMENSIONS,
                                    activation=tf.nn.softmax)(x)


model = tf.keras.Model(inputs = inputs, outputs = predictions)
optimizer = tf.train.AdamOptimizer(learning_rate = 0.001)
model.compile(loss ='categorical_crossentropy', optimizer = optimizer, metrics = ['accuracy'])


NUM_GPUS = 2
strategy = tf.contrib.distribute.MirroredStrategy(num_gpus=NUM_GPUS)
config = tf.estimator.RunConfig(train_distribute=strategy)
estimator = tf.keras.estimator.model_to_estimator(model,
                                                  config=config)

def input_fn(images, labels, epochs, batch_size):
    # Convert the inputs to a Dataset. (E)
    ds = tf.data.Dataset.from_tensor_slices((images, labels))
    # Shuffle, repeat, and batch the examples. (T)
    SHUFFLE_SIZE = 5000
    ds = ds.shuffle(SHUFFLE_SIZE).repeat(epochs).batch(batch_size)
    ds = ds.prefetch(2)
    # Return the dataset. (L)
    return ds


class TimeHistory(tf.train.SessionRunHook):
    def begin(self):
        self.times = []

    def before_run(self, run_context):
        self.iter_time_start = time.time()

    def after_run(self, run_context, run_values):
        self.times.append(time.time() - self.iter_time_start)



BATCH_SIZE = 512
EPOCHS = 5

time_hist = TimeHistory()

estimator.train(input_fn=lambda:input_fn(train_images,
                                         train_labels,
                                         epochs=EPOCHS,
                                         batch_size=BATCH_SIZE),
                hooks=[time_hist])


total_time = sum(time_hist.times)
print(f"total time with {NUM_GPUS} GPUs: {total_time} seconds")


avg_time_per_batch = np.mean(time_hist.times)
print(f"{BATCH_SIZE*NUM_GPUS/avg_time_per_batch} images/second with {NUM_GPUS} GPUs")

estimator.evaluate(lambda:input_fn(test_images,
                                   test_labels,
                                   epochs=1,
                                   batch_size=BATCH_SIZE))



print(1)