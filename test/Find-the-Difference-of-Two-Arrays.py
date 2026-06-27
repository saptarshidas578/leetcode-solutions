1class Solution:
2    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
3        s1=set(nums1)
4        s2=set(nums2)
5        l=[[],[]]
6        for i in s1:
7            if i not in s2:
8                l[0].append(i)
9        for j in s2:
10            if j not in s1:
11                l[1].append(j)
12        return l
13       
14
15        