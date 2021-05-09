class Solution(object):
    def find_path(self,grid,i,j,num = 0):
        path = []
        if i >0 and grid[i-1][j] ==num:
            path.append([i-1,j])
        if i < self.m-1 and grid[i+1][j] == num:
            path.append([i+1,j])
        if j >0 and grid[i][j-1] == num:
            path.append([i,j-1])
        if j < self.n -1 and grid[i][j+1] == num:
            path.append([i,j+1])
        return path

    def dfs(self,grid,i,j,count):
        if count ==0 and len(self.find_path(grid,i,j,num=2)) == 1:
            self.res += 1
            return
        # grid[i][j] = -1
        path = self.find_path(grid,i,j)
        for path_i,path_j in path:
            grid[i][j] = -1
            self.dfs(grid,path_i,path_j,count-1)
            grid[i][j] = 0

    def uniquePathsIII(self, grid):
        self.m = len(grid)
        self.n = len(grid[0])
        count = 0
        self.res = 0
        for i in range(self.m):
            for j in range(self.n):
                if grid[i][j] == 1:
                    beg_i,beg_j = i,j
                if grid[i][j] == 0:
                    count += 1

        self.dfs(grid,beg_i,beg_j,count)
        return self.res
