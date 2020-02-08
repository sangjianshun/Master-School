class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        res = [1]
        for i in range(1,len(ratings)):
            if ratings[i]>ratings[i-1]:
                res.append(res[-1]+1)
            else:
                res.append(1)
        for i in range(len(ratings)-2,-1,-1):
            if ratings[i]>ratings[i+1]:
                res[i] = max(res[i],res[i+1] +1)
        return sum(res)
print(Solution().candy([4,7,5,3,6,7]))
