# encoding=utf-8
import sys

def judge_continue(x):
    #去掉将牌看现在是不是可以凑ABC或者AAA
    if len(x)==0:
        return True
    if len(x)%3!=0:
        return False
    if x[0] == x[1] and x[0]==x[2]:
        return judge_continue(x[3:])
    if x[0] + 1 not in x or x[0] + 2 not in x:
        return False
    else:
        tmp = x[0]
        x.remove(tmp)
        x.remove(tmp + 1)
        x.remove(tmp + 2)
        return judge_continue(x)


def judge(x):
    #判断能不能胡
    x = sorted(x)
    if len(x)==2:
        if x[0] == x[1]:
            return True
        else:
            return False
    #找将牌
    general = []
    for i in range(1,10):
        if i in x:
            index = x.index(i)
            if index != len(x)-1:
                if x[index+1] == i:
                    general.append(i)
    for gen in general:
        tmp = [item for item in x]
        tmp.remove(gen)
        tmp.remove(gen)
        if judge_continue(tmp):
            return True
    return False

# if judge([1,1,1,2,3,4,4,4,4,5,5]):
#     print("胡了")
# else:
#     print("没叫随便打")

def fun(x):
    len_pai = [2,5,8,11,14]
    if len(x) not in len_pai:
        print("你手上牌张数有问题，多半是杠没有摸牌。")
        return
    x = sorted(x)
    if x[0]<1:
        print("最小的牌应该是1")
        return
    if x[-1]>9:
        print("最大的牌应该是9")
        return
    if judge(x):
        print("不好意思，自摸三家")
        return
    hand = []
    for i in range(1,10):
        if i in x and i not in hand:
            hand.append(i)
    result = []
    for item in hand:
        tmp = [_ for _ in x]
        tmp.remove(item)
        for i in range(1,10):
            tmp2 = [_ for _ in tmp]
            tmp2.append(i)
            if judge(tmp2):
                if [item,i] not in result:
                    result.append([item,i])
    dic = {}
    for item in result:
        try:
            dic[item[0]].append(item[1])
        except:
            dic[item[0]]=[item[1]]
    for item in dic:
        print("打{},胡{}".format(item,dic[item]))
while True:
    print("请输入你现在手上的牌")
    x = sys.stdin.readline().strip()
    x = list(map(int, x))
    fun(x)
# [2,2,2,3,4,5,6,7,8,9,3]
# 22234567893
