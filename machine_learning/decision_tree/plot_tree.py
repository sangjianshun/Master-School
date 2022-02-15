import matplotlib.pyplot as plt

plt.rcParams['font.family'] = ['Fangsong']


def getNumLeafs(myTree):
    numLeafs = 0
    firstStr = list(myTree.keys())[0]
    secondDict = myTree[firstStr]
    for key in secondDict.keys():
        if type(secondDict[key]).__name__ == 'dict':
            numLeafs += getNumLeafs(secondDict[key])
        else:
            numLeafs += 1
    return numLeafs


def getTreeDepth(myTree):
    maxDepth = 0
    firstStr = list(myTree.keys())[0]
    secondDict = myTree[firstStr]
    for key in secondDict.keys():
        if type(secondDict[key]).__name__ == 'dict':
            thisDepth = 1 + getTreeDepth(secondDict[key])
        else:
            thisDepth = 1
        if thisDepth > maxDepth: maxDepth = thisDepth
    return maxDepth


decisionNode = dict(boxstyle="sawtooth", fc="0.8")  # boxstyle为文本框的类型，sawtooth是锯齿形，fc是边框线粗细
leafNode = dict(boxstyle="round4", fc="0.8")  # round4表示圆形
arrow_args = dict(arrowstyle="<-")  # 箭头样式


def plotNode(nodeTxt, centerPt, parentPt, nodeType):
    plot_tree.ax1.annotate(nodeTxt, xy=parentPt, xycoords='axes fraction',
                           xytext=centerPt, textcoords='axes fraction',
                           va="center", ha="center", bbox=nodeType, arrowprops=arrow_args)


def plotMidText(cntrPt, parentPt, txtString):
    xMid = (parentPt[0] - cntrPt[0]) / 2.0 + cntrPt[0]  # 计算标注位置
    yMid = (parentPt[1] - cntrPt[1]) / 2.0 + cntrPt[1]
    plot_tree.ax1.text(xMid, yMid, txtString, va="center", ha="center", rotation=30)


def plotTree(myTree, parentPt, nodeTxt):
    numLeafs = getNumLeafs(myTree)
    depth = getTreeDepth(myTree)
    firstStr = list(myTree.keys())[0]  # 找到第一个元素，根节点
    cntrPt = (plotTree.xOff + (1.0 + float(numLeafs)) / 2.0 / plotTree.totalW, plotTree.yOff)  # 节点位置

    plotMidText(cntrPt, parentPt, nodeTxt)  # 标记子节点属性值
    plotNode(firstStr, cntrPt, parentPt, decisionNode)
    secondDict = myTree[firstStr]  # 获取节点下的内容
    plotTree.yOff = plotTree.yOff - 1.0 / plotTree.totalD  # 减少 y 偏移，树是自顶向下画的
    for key in secondDict.keys():  # 键值：0、1
        if type(secondDict[key]).__name__ == 'dict':  # 判断是 dict 还是 value
            plotTree(secondDict[key], cntrPt, str(key))  # 递归调用
        else:
            plotTree.xOff = plotTree.xOff + 1.0 / plotTree.totalW  # 更新 x 值
            plotNode(secondDict[key], (plotTree.xOff, plotTree.yOff), cntrPt, leafNode)
            plotMidText((plotTree.xOff, plotTree.yOff), cntrPt, str(key))
    plotTree.yOff = plotTree.yOff + 1.0 / plotTree.totalD


def plot_tree(inTree):
    fig = plt.figure(1, facecolor='white')
    fig.clf()
    axprps = dict(xticks=[], yticks=[])
    plot_tree.ax1 = plt.subplot(111, frameon=False, **axprps)  # 定义绘图区
    plotTree.totalW = float(getNumLeafs(inTree))  # 存储树的宽度
    plotTree.totalD = float(getTreeDepth(inTree))  # 存储树的深度

    # 使用了这两个全局变量追踪已经绘制的节点位置，以及放置下一个节点的恰当位置
    plotTree.xOff = -0.5 / plotTree.totalW;
    plotTree.yOff = 1.0;
    plotTree(inTree, (0.5, 1.0), ' ')
    plt.show()


# 转变树的存储方式
def treeNode2Dict(TreeNode, res):
    if not TreeNode.feature:
        return TreeNode.value
    if TreeNode.feature:
        res[TreeNode.feature] = {}
    if TreeNode.left:
        key = '<=' + str(TreeNode.value)
        res[TreeNode.feature][key] = treeNode2Dict(TreeNode.left, {})
    if TreeNode.right:
        key = '>' + str(TreeNode.value)
        res[TreeNode.feature][key] = treeNode2Dict(TreeNode.right, {})
    return res
