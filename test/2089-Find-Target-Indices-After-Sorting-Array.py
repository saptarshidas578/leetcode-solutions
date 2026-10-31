class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        nums.sort()
        i=0
        ans=[]
        while target in nums:
            ans.append(nums.index(target)+i)
            nums.remove(target)
            i+=1
        else:
            return ans
        return []

        