import numpy as np

from machine_learning.decision_tree.decision_tree import createDataSetForRegression, createValidDataSetForRegression
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


def gen_leaf(dataSet):
    """生成叶子节点，即目标变量的均值"""
    return np.mean(dataSet[:, -1])


def cal_square_error(all_label):
    square_error = np.var(all_label) * len(all_label)
    return square_error


def choose_feature(dataset, threhold_leaf, threhold_SE):
    if len(set(dataset[:, -1])) == 1:
        # 如果这个特征已经是唯一的，不可再分
        return None, dataset[0, -1]
    base_SE = cal_square_error(dataset[:, -1])
    n = dataset.shape[1]
    best_index = 0
    best_value = 0

    min_SE = np.inf
    for i in range(n - 1):
        if len(set(dataset[:, i])) == 1:
            continue
        for value in set(dataset[:, i]):
            dataset_left, dataset_right = split_dataset(dataset, i, value)
            # 如果这个特征已经是唯一的，不可再分
            if len(dataset_left) == 0 or len(dataset_right) == 0:
                continue
            new_loss = cal_square_error(dataset_left[:, -1]) + cal_square_error(dataset_right[:, -1])
            if new_loss < min_SE:
                min_SE = new_loss
                best_index = i
                best_value = value
    # 预剪枝1：平方误差下降量没有收益
    if (base_SE - min_SE) < threhold_SE:
        return None, gen_leaf(dataset)
    # 预剪枝2：叶子节点过少
    dataset_left, dataset_right = split_dataset(dataset, best_index, best_value)
    if (dataset_left.shape[0] < threhold_leaf) or (dataset_left.shape[1] < threhold_leaf):
        return None, gen_leaf(dataset)
    return best_index, best_value


def create_cart_regression_tree(dataset, column_name, threhold_leaf = -1, threhold_SE=0.01):
    feature, value = choose_feature(dataset,threhold_leaf, threhold_SE)
    # 如果feature为None, 则返回叶结点对应的预测值
    if feature == None:
        return TreeNode(feature, value)
    treeNode = TreeNode(column_name[feature], value)
    dataset_left, dataset_right = split_dataset(dataset, feature, value)
    treeNode.left = create_cart_regression_tree(dataset_left, column_name, threhold_leaf, threhold_SE)
    treeNode.right = create_cart_regression_tree(dataset_right, column_name, threhold_leaf, threhold_SE)
    return treeNode


if __name__ == '__main__':
    train_dataset, column_name = createDataSetForRegression()
    train_dataset = np.array(train_dataset)

    # 预剪枝
    cart_regression_tree = create_cart_regression_tree(train_dataset, column_name, threhold_leaf = -1, threhold_SE=0.01)
    res = treeNode2Dict(cart_regression_tree, {})
    plot_tree(res)
    valid_dataset, column_name = createValidDataSetForRegression()
    valid_dataset = np.array(valid_dataset)



