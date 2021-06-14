def cal_gini(prob_list):
    assert float(sum(prob_list)) == 1
    gini = 0
    for item in prob_list:
        gini += item ** 2
    return 1 - gini

def cal_gini_index(total_count, Dv):
    gini_index = 0
    for i in range(len(Dv)):
        Dv_count = sum(Dv[i])
        prob_list = [item / Dv_count for item in Dv[i]]
        gini_index += Dv_count/total_count * cal_gini(prob_list)
    return gini_index

if __name__ == '__main__':
    print(cal_gini_index(8,[[3,0],[2,3]]))
    print(cal_gini_index(8,[[2,1],[4,1]]))
    print(cal_gini_index(8,[[2,1],[0,3],[1,1]]))
    print(cal_gini_index(8,[[1,1],[4,2]]))
    print(cal_gini_index(5,[[2,1],[2,0]]))
    print(cal_gini_index(5,[[1,0],[2,2]]))