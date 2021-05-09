class Solution():
    def getMaxMatirx(self,matrix):
        self.m = len(matrix)
        self.n = len(matrix[0])
        dp = [[0 for j in range(self.n)] for i in range(self.m+1)]
        for i in range(1,self.m+1):
            for j in range(self.n):
                dp[i][j] = dp[i-1][j] + matrix[i-1][j]
        res = 0
        for i in range(1,self.m+1):
            for j in range(i,self.m+1):
                tmp = 0
                for k in range(self.n):
                    tmp += (dp[j][k] - dp[i-1][k])
                    if tmp <=0:
                        tmp = 0
                    else:
                        if tmp>res:
                            res = tmp
        return res
