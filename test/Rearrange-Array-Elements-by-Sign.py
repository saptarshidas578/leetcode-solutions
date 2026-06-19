1class Solution:
2    def rearrangeArray(self, nums: List[int]) -> List[int]:
3        n = len(nums)
4        ans = [0] * n
5
6        pos = 0   
7        neg = 1  
8
9        for num in nums:
10            if num > 0:
11                ans[pos] = num
12                pos += 2
13            else:
14                ans[neg] = num
15                neg += 2
16
17        return ans
18      
19        
20        