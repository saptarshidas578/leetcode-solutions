1class Solution:
2    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
3        l1=list(ransomNote)
4        l2=list(magazine)
5        for i in l1:
6            if i in l2:
7                l2.remove(i)
8            else:
9                return(False)
10        else:
11            return(True)
12
13        