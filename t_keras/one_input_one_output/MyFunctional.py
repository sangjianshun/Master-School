from tensorflow.python.keras import Input, Model
from tensorflow.python.keras.layers import Flatten, Dense, Dropout


class MyFunctional():
    def model_dnn(self):
        input_x = Input(shape=(28,28),name="input_layer")
        x = Flatten(name="flatten_layer")(input_x)
        x = Dense(256, 'relu', name="dense1_layer")(x)
        output = Dense(10, 'softmax', name="dense2_layer")(x)
        model = Model(inputs=input_x, outputs=output)
        return model


