1class Solution:
2    def mergeAlternately(self, word1: str, word2: str) -> str:
3        n1=len(word1)
4        n2=len(word2)
5        ans=""
6        if n1>n2:
7            try:
8                for i in range(n1):
9                    ans=ans+word1[i]+word2[i]
10            except:
11                ans=ans+word1[i:]
12        else:
13            try:
14                for i in range(n2):
15                    ans=ans+word1[i]+word2[i]
16            except:
17                ans=ans+word2[i:]
18        return(ans)
19
20
21        