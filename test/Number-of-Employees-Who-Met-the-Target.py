1class Solution:
2    from collections import Counter
3    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
4        d=Counter(hours)
5        s=0
6        for i in d:
7            if i>=target:
8                s+=d[i]
9        return s
10        