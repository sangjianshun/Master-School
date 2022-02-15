import numpy as np

from machine_learning.decision_tree.decision_tree import createDataSetForRegression
from plot_tree import plot_tree, treeNode2Dict


class TreeNode():
    def __init__(self, feature, value):
        self.feature = feature
        self.value = value
        self.left = None
        self.right = None


def split_dataset(dataset, feature_index, value):
    dataset_left = dataset[np.nonzero(dataset[:, feature_index] <= value)[0]]
    dataset_right = dataset[np.nonzero(dataset[:, feature_index] > value)[0]]
    return dataset_left, dataset_right


def regLeaf(dataSet):
    """生成叶子节点，即目标变量的均值"""
    return np.mean(dataSet[:, -1])


def cal_square_error(all_label):
    square_error = np.var(all_label) * len(all_label)
    return square_error


def choose_feature(dataset):
    if len(set(dataset[:, -1])) == 1:
        return None, dataset[0, -1]
    cal_square_error(dataset[:, -1])
    m, n = dataset.shape
    best_index = 0
    best_value = 0

    max_loss = np.inf
    for i in range(n - 1):
        if len(set(dataset[:, i])) == 1:
            continue
        for value in set(dataset[:, i]):
            dataset_left, dataset_right = split_dataset(dataset, i, value)
            # 如果这个特征已经是唯一的，不可再分
            if len(dataset_left) == 0 or len(dataset_right) == 0:
                continue
            new_loss = cal_square_error(dataset_left[:, -1]) + cal_square_error(dataset_right[:, -1])
            if new_loss < max_loss:
                max_loss = new_loss
                best_index = i
                best_value = value
    return best_index, best_value


def create_cart_regression_tree(dataset, column_name):
    feature, value = choose_feature(dataset)
    # 如果feat为None, 则返回叶结点对应的预测值
    if feature == None:
        return TreeNode(feature, value)
    treeNode = TreeNode(column_name[feature], value)
    dataset_left, dataset_right = split_dataset(dataset, feature, value)
    treeNode.left = create_cart_regression_tree(dataset_left, column_name)
    treeNode.right = create_cart_regression_tree(dataset_right, column_name)
    return treeNode


if __name__ == '__main__':
    dataset, column_name = createDataSetForRegression()
    dataset = np.array(dataset)

    cart_regression_tree = create_cart_regression_tree(dataset, column_name)

    res = treeNode2Dict(cart_regression_tree, {})
    plot_tree(res)

    # 剪枝代码讲解需要
    # def loadDataSet(fileName):      #general function to parse tab -delimited floats
    #     dataMat = []                #assume last column is target value
    #     fr = open(fileName)
    #     for line in fr.readlines():
    #         curLine = line.strip().split('\t')
    #         fltLine = list(map(float,curLine)) #map all elements to float()
    #         dataMat.append(fltLine)
    #     return dataMat
    # dataset = loadDataSet('./data/ex00.txt')
    # dataset = np.array(dataset)[:10,:]
    # column_name = ['feature1']
    # cart_regression_tree = create_cart_regression_tree(dataset, column_name)
    # res = treeNode2Dict(cart_regression_tree, {})
    # plot_tree(res)
    # print(1)
