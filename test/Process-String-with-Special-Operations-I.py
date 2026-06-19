1class Solution:
2    def processStr(self, s: str) -> str:
3        l=[]
4        for i in s:
5            if i=="#":
6                l=l*2
7            elif i=="*":
8                if l:
9                    l.pop()
10            elif i=="%":
11                l=l[::-1]
12            else:
13                l.append(i)
14        return "".join(l)
15
16        