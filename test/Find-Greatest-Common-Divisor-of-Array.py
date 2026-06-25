1class Solution:
2    from math import gcd
3    def findGCD(self, nums: List[int]) -> int:
4        return gcd(max(nums),min(nums))
5        