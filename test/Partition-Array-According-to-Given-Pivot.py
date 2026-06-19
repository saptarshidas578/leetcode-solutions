1class Solution:
2    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
3            less=[]
4            more=[]
5            ans=[]
6            for i in nums:
7                if i<pivot:
8                    less.append(i)
9                elif i>pivot:
10                    more.append(i)
11                else:
12                    ans.append(i)
13            return less+ans+more
14
15
16        