class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            nums[i]=nums[i]**2
        nums.sort()
        print(nums)
        return sum(nums[len(nums)//2:])-sum(nums[0:len(nums)//2])
        """else:
            return sum(nums[len(nums)//2:])-sum(nums[0:len(nums)//2])"""

        