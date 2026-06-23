1class Solution:
2    def pivotIndex(self, nums: List[int]) -> int:
3        if sum(nums[1:])==0:
4            return 0
5        else:
6            for i in range(1,len(nums)):
7                if i==len(nums)-1:
8                    if sum(nums[0:len(nums)-1])==0:
9                        return i
10                    else:
11                        return -1
12                if sum(nums[0:i])==sum(nums[i+1:]):
13                    return i
14            return -1
15
16        