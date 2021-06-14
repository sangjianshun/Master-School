from math import log

def cal_Ent(prob_list):
    assert float(sum(prob_list)) == 1
    Ent = 0.0
    for prob in prob_list:
        if prob == 0:
            continue
        Ent -= prob * log(prob, 2)
    return Ent

def cal_Gain(EntD,EntDv):
    """

    :param EntD:
    :param EntDv: [[3/8,0],[5/8,0.97]]
    :return:
    """
    total = 0
    Gain = EntD
    for i in range(len(EntDv)):
        total += EntDv[i][0]
        Gain -= EntDv[i][0] * EntDv[i][1]
    assert float(total) == 1
    return Gain

def cal_Gain_Ratio(Gain, Ent_a):
    return Gain/Ent_a




if __name__ == '__main__':
    # print(cal_Ent([3/8, 5/8]))
    # print(cal_Ent([1/2, 1/2, 0]))
    # print(cal_Ent([2/5, 3/5]))
    # print(cal_Ent([2/3,1/3]))
    # print(cal_Ent([1/5, 4/5]))
    # print(cal_Ent([3/8, 3/8, 2/8]))
    # print(cal_Ent([2/5, 2/5, 1/5]))

    # print(cal_Gain(0.95, [[3/8,0],[5/8,0.97]]))
    # print(cal_Gain(0.95, [[3/8,0.92],[5/8,0.72]]))
    # print(cal_Gain(0.95, [[3/8,0.92],[3/8,0],[2/8,1]]))
    print(cal_Gain(0.97, [[3/5,0.92],[2/5,0]]))
    #
    # print(cal_Gain(0.92, [[2/3,1],[1/3,0]]))
    print(cal_Gain_Ratio(0.34,0.95))
    print(cal_Gain_Ratio(0.16,0.95))
    print(cal_Gain_Ratio(0.36,1.56))
    print(cal_Gain_Ratio(0.97,1.52))
    print(cal_Gain_Ratio(0.42,0.97))