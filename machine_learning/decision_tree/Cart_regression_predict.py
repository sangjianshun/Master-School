from Cart_regression_with_pos_prune import prune
from Cart_regression_with_pre_prune import *
from machine_learning.decision_tree.decision_tree import createDataSetForRegression, createValidDataSetForRegression
from plot_tree import plot_tree, treeNode2Dict


def cart_regression_tree_pred_dataset(tree, column_name, dataset):
    pred = []
    label = []
    for i in range(len(dataset)):
        label.append(dataset[i, -1])
        pred.append(cart_regression_tree_pred(tree, column_name, dataset[i, :-1]))
    return label, pred


def cal_MSE(label, pred):
    err = np.array(label) - np.array(pred)
    se = np.square(err)
    mse = np.sum(se) / len(label)
    return mse


def cart_regression_tree_pred(tree, column_name, x):
    if not tree.feature:
        return tree.value
    index = column_name.index(tree.feature)
    if x[index] <= tree.value:
        return cart_regression_tree_pred(tree.left, column_name, x)
    else:
        return cart_regression_tree_pred(tree.right, column_name, x)


if __name__ == '__main__':
    train_dataset, column_name = createDataSetForRegression()
    train_dataset = np.array(train_dataset)

    valid_dataset, column_name = createValidDataSetForRegression()
    valid_dataset = np.array(valid_dataset)

    # 不剪枝产生的树
    cart_regression_tree_no_prune = create_cart_regression_tree(train_dataset, column_name, 1, 0.0000001)
    # 后剪枝产生的树
    cart_regression_tree = create_cart_regression_tree(train_dataset, column_name, 1, 0.0000001)
    cart_regression_tree_pos = prune(cart_regression_tree, valid_dataset, column_name)
    # 预剪枝产生的树
    cart_regression_tree_pre = create_cart_regression_tree(train_dataset, column_name, threhold_leaf=-1,
                                                           threhold_SE=0.01)

    print("#######################")
    # 未剪枝的mse:1.训练集 2.验证集
    label, pred = cart_regression_tree_pred_dataset(cart_regression_tree_no_prune, column_name, train_dataset)
    train_mse = cal_MSE(label, pred)
    print(label, pred)
    print(train_mse)

    label, pred = cart_regression_tree_pred_dataset(cart_regression_tree_no_prune, column_name, valid_dataset)
    valid_mse = cal_MSE(label, pred)
    print(label, pred)
    print(valid_mse)

    # 预剪枝的mse:1.训练集 2.验证集
    print("#######################")
    label, pred = cart_regression_tree_pred_dataset(cart_regression_tree_pre, column_name, train_dataset)
    train_mse = cal_MSE(label, pred)
    print(label, pred)
    print(train_mse)

    label, pred = cart_regression_tree_pred_dataset(cart_regression_tree_pre, column_name, valid_dataset)
    valid_mse = cal_MSE(label, pred)
    print(label, pred)
    print(valid_mse)

    # 后剪枝的mse:1.训练集 2.验证集
    print("#######################")
    label, pred = cart_regression_tree_pred_dataset(cart_regression_tree_pos, column_name, train_dataset)
    train_mse = cal_MSE(label, pred)
    print(label, pred)
    print(train_mse)

    label, pred = cart_regression_tree_pred_dataset(cart_regression_tree_pos, column_name, valid_dataset)
    valid_mse = cal_MSE(label, pred)
    print(label, pred)
    print(valid_mse)

    print(1)
