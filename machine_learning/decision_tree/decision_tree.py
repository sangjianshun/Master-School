# 未完待续

def createDataSet():
    """
    工资：1高，0低
    压力：1小，0：大
    平台：2第一梯队，1第二梯队，0第三梯队
    """
    dataSet = [[1, 1, 2, '好'],
               [0, 1, 0, '好'],
               [1, 0, 0, '好'],
               [0, 1, 0, '好'],
               [0, 1, 1, '不好'],
               [1, 1, 1, '好'],
               [0, 0, 2, '不好'],
               [0, 0, 1, '不好']]
    column_name = ['工资', '压力', '平台']
    return dataSet, column_name

def createDataSetForRegression():
    dataSet = [[1, 1, 2, 1],
               [0, 1, 0, 0.9],
               [1, 0, 0, 0.8],
               [0, 1, 0, 0.9],
               [0, 1, 1, 0.1],
               [1, 1, 1, 0.9],
               [0, 0, 2, 0.2],
               [0, 0, 1, 0.1]]
    column_name = ['工资', '压力', '平台']
    return dataSet, column_name

"""

"""
print(1)