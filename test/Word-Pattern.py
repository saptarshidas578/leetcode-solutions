1class Solution:
2    def wordPattern(self, pattern: str, s: str) -> bool:
3        pat=list(pattern)
4        sl=s.split()
5        return list(map(pat.index,pat))==list(map(sl.index,sl))
6        