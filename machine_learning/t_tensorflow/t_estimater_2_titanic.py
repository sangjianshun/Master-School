import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import sklearn
import pandas as pd
import os
import sys
import time
import tensorflow as tf
from tensorflow import keras
# 打印版本
print(tf.__version__)
print(sys.version_info)
for module in mpl,np,pd,sklearn,tf,keras:
    print(module.__name__, module.__version__)

file_name = './dataset/titanic.csv'
file_name = './dataset/train.csv'
df = pd.read_csv(file_name)

train_df = df
test_df = train_df.sample(frac=0.2)
train_df = train_df[~train_df.index.isin(test_df.index)]

train_df_y = train_df.pop('survived')
test_df_y = test_df.pop('survived')

print(len(train_df), len(test_df))



columns = ['survived', 'sex', 'age', 'n_siblings_spouses', 'parch', 'fare', 'class', 'deck', 'embark_town', 'alone']

categorical = ['sex', 'n_siblings_spouses', 'parch', 'class', 'deck', 'embark_town', 'alone']
numeric = ['age', 'fare']

# columns = ["pclass","survived","name","age","embarked","home.dest","room","ticket","boat","sex"]
#
# categorical = ["pclass","name","embarked","home.dest","room","ticket","boat","sex"]
# numeric = ['age' ]


features = []
for feature in categorical:
    features.append(
        tf.feature_column.indicator_column(
            tf.feature_column.categorical_column_with_vocabulary_list(
                feature, train_df[feature].unique()))
    )

for feature in numeric:
    features.append(
        tf.feature_column.numeric_column(feature, dtype=tf.float32)
    )

def train_input_fn(features, labels, batch_size=8):
    dataset = tf.data.Dataset.from_tensor_slices((dict(features), labels))
    dataset = dataset.shuffle(len(train_df))
    dataset = dataset.repeat(30000)
    return dataset.batch(batch_size)
def test_input_fn(features, labels, batch_size=8):
    dataset = tf.data.Dataset.from_tensor_slices((dict(features), labels))
    return dataset.batch(batch_size)

train_fn = lambda: train_input_fn(train_df, train_df_y)
test_fn = lambda: test_input_fn(test_df, test_df_y)

classifier = tf.estimator.DNNClassifier(
    feature_columns=features,
    hidden_units=[50, 30, 20],
    n_classes=2)

classifier.train(input_fn=train_fn, steps=30000)

test_result = classifier.evaluate(input_fn=test_fn)
print(test_result)


print(1)