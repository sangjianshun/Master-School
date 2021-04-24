import numpy as np


def HammingLoss(label, predict):
    # label: (N, D)
    D = len(label[0])
    N = len(label)
    tmp = 0
    for i in range(N):
        tmp = tmp + np.sum(label[i] ^ predict[i])
    hamming_loss = tmp / N / D
    return hamming_loss


def Coverage(label, logit):
    D = len(label[0])
    N = len(label)
    label_index = []
    for i in range(N):
        index = np.where(label[i] == 1)[0]
        label_index.append(index)
    cover = 0
    for i in range(N):
        # 从大到小排序
        index = np.argsort(-logit[i]).tolist()
        tmp = 0
        for item in label_index[i]:
            tmp = max(tmp, index.index(item) + 1)
        cover += tmp
    coverage = cover * 1.0 / N
    return coverage


def One_error(label, logit):
    N = len(label)
    for i in range(N):
        if max(label[i]) == 0:
            print("该条数据哪一类都不是")
    label_index = []
    for i in range(N):
        index = np.where(label[i] == 1)[0]
        label_index.append(index)
    OneError = 0
    for i in range(N):
        if np.argmax(logit[i]) not in label_index[i]:
            OneError += 1
    OneError = OneError * 1.0 / N
    return OneError


def Average_Precision(label, logit):
    N = len(label)
    for i in range(N):
        if max(label[i]) == 0 or min(label[i]) == 1:
            print("该条数据哪一类都不是或者全都是")
    precision = 0
    for i in range(N):
        index = np.where(label[i] == 1)[0]
        score = logit[i][index]
        score = sorted(score)
        score_all = sorted(logit[i])
        precision_tmp = 0
        for item in score:
            tmp1 = score.index(item)
            tmp1 = len(score) - tmp1
            tmp2 = score_all.index(item)
            tmp2 = len(score_all) - tmp2
            precision_tmp += tmp1 / tmp2
        precision += precision_tmp / len(score)
    Average_Precision = precision / N
    return Average_Precision


def RankingLoss(label, logit):
    N = len(label)
    for i in range(N):
        if max(label[i]) == 0 or min(label[i]) == 1:
            print("该条数据哪一类都不是或者全都是")
    rankloss = 0
    for i in range(N):
        index1 = np.where(label[i] == 1)[0]
        index0 = np.where(label[i] == 0)[0]
        tmp = 0
        for j in index1:
            for k in index0:
                if logit[i][j] <= logit[i][k]:
                    tmp += 1
        rankloss += tmp * 1.0 / ((len(index1)) * len(index0))
    rankloss = rankloss / N
    return rankloss


logit = np.array([[0.3, 0.4, 0.5, 0.1, 0.15]])
label = np.array([[1, 0, 1, 0, 0]])
pred = np.array([[0, 1, 1, 0, 0]])

print(HammingLoss(label, pred))
