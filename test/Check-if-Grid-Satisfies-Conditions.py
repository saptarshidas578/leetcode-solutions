1class Solution:
2    def satisfiesConditions(self, grid: List[List[int]]) -> bool:
3        n=len(grid)
4        m=len(grid[0])
5        for i in range(n):
6            for j in range(m-1):
7                if grid[i][j]==grid[i][j+1]:
8                    return False
9        for k in range(m):
10            for j in range(n-1):
11                if grid[j][k]!=grid[j+1][k]:
12                    return False
13        return True
14