1class Solution:
2    def leftRightDifference(self, nums: List[int]) -> List[int]:
3        if len(nums)==1:
4            return [0]
5        ans=[]
6        ans.append(abs(sum(nums[1:])))
7        for i in range(1,len(nums)-1):
8            ans.append(abs(sum(nums[i+1:])-sum(nums[0:i])))
9        
10        ans.append(abs(sum(nums[0:len(nums)-1])))
11        return(ans)
12        