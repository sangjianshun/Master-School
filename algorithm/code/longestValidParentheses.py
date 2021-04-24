class Solution(object):
    def longestValidParentheses(self, s):
        len_s = len(s)
        if len_s<2:
            return 0
        dp = [0 for i in range(len_s)]
        for i in range(1,len_s):
            if s[i] == ")":
                if i-1-dp[i-1]>=0 and s[i-1-dp[i-1]] =="(":
                    dp[i] = dp[i-1] +2
                    if i- dp[i] >0:
                        dp[i] += dp[i-dp[i]]
                else: dp[i] =0
            else: dp[i] = 0
        return max(dp)
