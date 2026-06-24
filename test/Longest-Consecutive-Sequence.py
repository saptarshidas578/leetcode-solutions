1class Solution:
2    def longestConsecutive(self, nums: List[int]) -> int:
3        nums=list(set(nums))
4        nums.sort()
5        ans=[]
6        c=1
7        if len(nums)==0:
8            return 0
9        for i in range(len(nums)-1):
10            if nums[i+1]-nums[i]==1:
11                c=c+1
12            else:
13                ans.append(c)
14                c=1
15        ans.append(c)
16        #print(nums)
17        #print(ans)
18        return max(ans)