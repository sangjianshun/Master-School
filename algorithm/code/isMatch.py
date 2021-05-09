class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        len_s = len(s)
        len_p = len(p)
        dp = [[False for i in range(len_p+1)] for j in range(len_s+1)] #这里要注意list的创建方法。
        dp[0][0] = True
        for i in range(len_s+1):
            for j in range(1, len_p+1):
                if p[j-1]=="*":
                    dp[i][j] = dp[i][j-2] or dp[i-1][j] and (s[i-1]==p[j-2] or p[j-2] == ".")
                else:
                    dp[i][j] = dp[i-1][j-1] and (s[i-1]==p[j-1] or p[j-1] == ".")
        return dp[-1][-1]
