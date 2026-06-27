1class Solution:
2    def intersection(self, nums: List[List[int]]) -> List[int]:
3        l=[]
4        c=0
5        for i in nums[0]:
6            for j in nums[1:]:
7                if i not in j:
8                    break
9            else:
10                l.append(i)
11        l.sort()
12        return(l)
13            
14                    