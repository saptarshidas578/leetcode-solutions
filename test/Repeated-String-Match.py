1class Solution:
2    def repeatedStringMatch(self, a: str, b: str) -> int:
3        n=1
4        s=a
5        while b not in a :
6            if len(a)>len(b):
7                break
8            a=a+s
9            n+=1
10        if b in a:
11            return n
12        elif b in a+s:
13            return n+1
14        else:
15            return(-1)
16        