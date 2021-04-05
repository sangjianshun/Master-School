import tensorflow as tf
from tensorflow.python.keras import Input
from tensorflow.python.keras.layers import Flatten, Dense


class MySequential():
    def model_dnn(self):
        model = tf.keras.models.Sequential()
        model.add(Input(shape=(28, 28,), name="input_layer"))
        model.add(Flatten(name="flatten_layer"))
        model.add(Dense(256, 'relu', name="dense1_layer"))
        model.add(Dense(10, 'softmax', name="dense2_layer"))

        # model = tf.keras.models.Sequential(
        #     Input(shape=(28, 28,), name="input_layer"),
        #     Flatten(name="flatten_layer"),
        #     Dense(256, 'relu', name="dense1_layer"),
        #     Dense(10, 'softmax', name="dense2_layer")
        # )
        return model

if __name__ == '__main__':
    mySequential = MySequential()
    model = mySequential.model_dnn()
    print(model.summary())
    print(model.weights)
    print(model.layers)
