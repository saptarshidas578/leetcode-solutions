1class Solution:
2    def numOfStrings(self, patterns: List[str], word: str) -> int:
3        c=0
4        for i in patterns:
5            if i in word:
6                c+=1
7        return c
8        