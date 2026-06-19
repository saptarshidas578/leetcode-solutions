1class Solution:
2    def numPairsDivisibleBy60(self, time: List[int]) -> int:
3        c=[0]*60
4        res=0
5        for t in time:
6            res+=c[-t%60]
7            c[t%60]+=1
8        return res
9        