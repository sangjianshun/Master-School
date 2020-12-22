import matplotlib.pyplot as plt
import numpy as np

def F1(P,R):
    return 2*P*R/(P+R)
def ROC(pos,neg):

    TPR = []
    FPR = []
    for i in np.arange(0.05,1,0.05):
        if i == 0.8:
            print(1)
        TP = 0
        FP = 0
        TN = 0
        FN = 0
        for item in pos:
            if item >=i: #预测为正
                TP +=1
            else: #预测为负
                FN +=1
        for item in neg:
            if item <i: #预测为负
                TN +=1
            else: #预测为正
                FP +=1
        TPR.append(TP/(TP+FN))
        FPR.append(FP/(FP+TN))
    plt.xlabel("FPR", fontsize=12)
    plt.ylabel("TPR", fontsize=12)
    plt.plot(FPR,TPR)
    plt.show()

def AUC(pos,neg):
    pos = sorted(pos)
    neg = sorted(neg)
    count = 0
    for pos1 in pos:
        for neg1 in neg:
            if pos1>neg1:
                count += 1
            elif pos1==neg1:
                count+=0.5
            else:
                break
    return count/(len(pos) *len(neg))
