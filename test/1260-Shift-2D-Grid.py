class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        l=[]
        rl=len(grid[0])
        ans=[]
        for i in grid:
            l.extend(i)
        for i in range(k):
            a=l.pop()
            l.insert(0,a)
        for i in range(0,len(l),rl):
            ans.append(l[i:i+rl])
        return ans
        
        
        