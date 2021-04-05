from tensorflow.python.keras import Model, Input
from tensorflow.python.keras.layers import Flatten, Dense, Dropout
import tensorflow as tf

class MyModelSubclass(Model):
    def __init__(self):
        Model.__init__(self)
        self.flatten = Flatten(name="flatten_layer")
        self.dense1 = Dense(256, 'relu', name="dense1_layer")
        self.dense2 = Dense(10, 'softmax', name="dense2_layer")

    def call(self, inputs):
        x = self.flatten(inputs)
        x = self.dense1(x)
        outputs = self.dense2(x)

        return outputs

    def build_graph(self, input_shape):
        input_x = Input(shape=input_shape, name="input_layer")
        outputs = Model(inputs=[input_x], outputs=self.call(input_x))
        return outputs


class BaseNetwork(tf.keras.models.Model):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.flatten_input = Flatten(name="flatten_input")
        self.first_base_dense = Dense(128, activation='relu', name="first_base_dense")
        self.first_dropout = Dropout(0.1, name="first_dropout")
        self.second_base_dense = Dense(128, activation='relu', name="second_base_dense")
        self.second_dropout = Dropout(0.1, name="second_dropout")
        self.third_base_dense = Dense(128, activation='relu', name="third_base_dense")

    def call(self, input_):
        output = self.flatten_input(input_)
        output = self.first_base_dense(output)
        output = self.first_dropout(output)
        output = self.second_base_dense(output)
        output = self.second_dropout(output)
        output = self.third_base_dense(output)
        return output
