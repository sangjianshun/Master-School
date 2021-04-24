
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates = sorted(candidates)
        self.res = []
        def dfs(res_tmp,candidates,target):
            for i in range(len(candidates)):
                if candidates[i] >target:
                    break
                elif candidates[i]==target:
                    res = res_tmp + [candidates[i]]
                    self.res.append(res)
                else:
                    res = res_tmp + [candidates[i]]

                    dfs(res, candidates[i:], target - candidates[i])
        dfs([],candidates,target)
        return self.res
