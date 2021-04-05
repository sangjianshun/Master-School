from tensorflow.python.keras import Sequential
from tensorflow.python.keras.datasets.mnist import load_data
from tensorflow.python.keras.utils.vis_utils import plot_model

from t_keras.one_input_one_output.MyFunctional import MyFunctional
from t_keras.one_input_one_output.MyModelSubclass import MyModelSubclass
from t_keras.one_input_one_output.MySequential import MySequential
from t_keras.util import show_image

(x_train, y_train), (x_test, y_test) = load_data('mnist.npz')

show_image(x_train[0], y_train[0])

# normalization
x_train = x_train.astype('float32')
x_test = x_test.astype('float32')
x_train /= 255  # 把数值变成0-1之间的浮点数。
x_test /= 255

# # 1、sequential
# mySequential = MySequential()
# model = mySequential.model_dnn()
# plot_model(model, show_shapes=True, show_layer_names=True, to_file='./image/mySequential.model_dnn.png')

# 2、functional
# myFunctional = MyFunctional()
# model = myFunctional.model_dnn()
# plot_model(model, show_shapes=True, show_layer_names=True, to_file='./image/myFunctional.model_dnn.png')

# 3、modelSubclass

model = MyModelSubclass()
model = model.build_graph((28,28))
plot_model(model, show_shapes=True, show_layer_names=True, to_file='./image/myModelSubclass.model_dnn.png')

# summary之前一定要built
model.summary()

model.compile(optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"])
model.fit(x=x_train, y=y_train, epochs=5)
model.evaluate(x=x_test, y=y_test)
print(model.predict(x_test)[:10])
print(model.summary())
