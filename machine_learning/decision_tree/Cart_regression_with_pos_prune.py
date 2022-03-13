from Cart_regression_with_pre_prune import *
from machine_learning.decision_tree.decision_tree import createDataSetForRegression, createValidDataSetForRegression
from plot_tree import plot_tree, treeNode2Dict


def get_mean(tree):
    if tree.right:
        tree.right = get_mean(tree.right)
    else:
        tree.right = tree.value
    if tree.left:
        tree.left = get_mean(tree.left)
    else:
        tree.left = tree.value
    return TreeNode(None,(tree.left + tree.right)/2.0)


def prune(tree, testData,column_name):
    # 没有测试数据，该位置应该是一个叶子节点
    if testData.shape[0] == 0:
        return get_mean(tree)
    if tree.right.feature or tree.left.feature:
        i = column_name.index(tree.feature)
        left_dataset, right_dataset = split_dataset(testData, i, tree.value)
    if tree.left.feature:
        tree.left = prune(tree.left, left_dataset,column_name)
    if tree.right.feature:
        tree.right = prune(tree.right, right_dataset,column_name)
    # 都是叶子节点，check是否需要合并
    if not tree.left.feature and not tree.right.feature:
        i = column_name.index(tree.feature)
        left_dataset, right_dataset = split_dataset(testData, i, tree.value)

        no_merge_SE = sum(np.power(left_dataset[:,-1] - tree.left.value, 2)) + \
                       sum(np.power(right_dataset[:,-1] - tree.right.value,2))
        tree_mean = (tree.left.value + tree.right.value)/2.0
        merge_SE = sum(np.power(testData[:,-1] - tree_mean,2))
        if merge_SE < no_merge_SE:
            print(f"{merge_SE} < {no_merge_SE} :merging")
            print(left_dataset[:,-1], right_dataset[:,-1])
            return TreeNode(None, tree_mean)
        else: return tree
    else: return tree


if __name__ == '__main__':
    train_dataset, column_name = createDataSetForRegression()
    train_dataset = np.array(train_dataset)


    valid_dataset, column_name = createValidDataSetForRegression()
    valid_dataset = np.array(valid_dataset)
    # 后剪枝
    cart_regression_tree = create_cart_regression_tree(train_dataset, column_name, threhold_leaf = -1, threhold_SE=0.001)
    # res = treeNode2Dict(cart_regression_tree, {})

    cart_regression_tree_pos = prune(cart_regression_tree, valid_dataset,column_name)
    cart_regression_tree_pos = treeNode2Dict(cart_regression_tree_pos, {})


    plot_tree(cart_regression_tree_pos)



