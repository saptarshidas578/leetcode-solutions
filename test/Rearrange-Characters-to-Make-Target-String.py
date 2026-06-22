1class Solution:
2    from collections import Counter
3    def rearrangeCharacters(self, s: str, target: str) -> int:
4        t=Counter(target)
5        s1=Counter(s)
6        l=[]
7        for i in t:
8            if i not in s1:
9                return 0
10            else:
11                l.append(s1[i]//t[i])
12        return min(l)
13        