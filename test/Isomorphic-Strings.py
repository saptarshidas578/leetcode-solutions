1class Solution:
2    def isIsomorphic(self, s: str, t: str) -> bool:
3        return list(map(s.index, s)) == list(map(t.index, t))
4