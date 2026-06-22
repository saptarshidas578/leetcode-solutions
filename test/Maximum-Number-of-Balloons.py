1class Solution:
2    def maxNumberOfBalloons(self, text: str) -> int:
3        t=Counter("balloon")
4        s1=Counter(text)
5        l=[]
6        for i in t:
7            if i not in s1:
8                return 0
9            else:
10                l.append(s1[i]//t[i])
11        return min(l)
12        