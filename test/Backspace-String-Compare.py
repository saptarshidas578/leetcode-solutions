1class Solution:
2    def backspaceCompare(self, s: str, t: str) -> bool:
3        l1=[]
4        l2=[]
5        for i in s:
6            if i!="#":
7                l1.append(i)
8            else:
9                if l1:
10                    l1.pop()
11        for j in t:
12            if j!="#":
13                l2.append(j)
14            else:
15                if l2:
16                    l2.pop()
17        return l1==l2
18        
19
20        
21        