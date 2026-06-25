1class Solution:
2    def numberOfCuts(self, n: int) -> int:
3        if n==1:
4            return 0
5        if n%2==0:
6            return n//2
7        else:
8            return n
9        