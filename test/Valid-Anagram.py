1class Solution:
2    from collections import Counter
3    def isAnagram(self, s: str, t: str) -> bool:
4        s1=Counter(s)
5        s2=Counter(t)
6        if len(s1)!=len(s2):
7            return False
8        try:
9            for i in s:
10                if s1[i]!=s2[i]:
11                    return False
12        except:
13            return False
14        return True
15        