1class Solution:
2    def reverseWords(self, s: str) -> str:
3        l=s.split()
4        l=l[::-1]
5        w=l[0]
6        for i in range(1,len(l)):
7            w=w+" "+l[i]
8        return w
9
10        