from tensorflow.python.keras import Model, Input

from t_keras.one_input_one_output.MyFunctional import MyFunctional
from t_keras.parameter_share.MyLayer import MyEuclideanDistanceLayer
from t_keras.one_input_one_output.MyModelSubclass import MyModelSubclass
from t_keras.parameter_share.functional_basenetwork import feature_extraction_for_siamese_network
from t_keras.util import euclidean_distance


class MySiameseModel(Model):
    def __init__(self):
        Model.__init__(self)
        self.layer_euclidean_distance = MyEuclideanDistanceLayer()
        self.base_network = feature_extraction_for_siamese_network()

    def call(self, inputs, training=None, mask=None):
        left_input, right_input = inputs
        left_feature = self.base_network(left_input)
        right_feature = self.base_network(right_input)
        # output = self.layer_euclidean_distance([left_feature, right_feature])
        output = euclidean_distance([left_feature, right_feature])
        return output

    def build_graph(self, input_shape):
        left_input = Input(input_shape)
        right_input = Input(input_shape)
        return Model(inputs=[left_input, right_input], outputs=self.call([left_input,right_input]))

def my_siamese_model(input_shape):
    baseNetwork = feature_extraction_for_siamese_network()
    left_input = Input(shape=input_shape, name="layer_left_input")
    right_input = Input(shape=input_shape, name="layer_right_input")

    left_feature = baseNetwork(left_input)
    right_feature = baseNetwork(right_input)
    output = euclidean_distance([left_feature, right_feature])
    model = Model(inputs=[left_input, right_input], outputs=output)
    return model

