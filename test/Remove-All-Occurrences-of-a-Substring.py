1class Solution:
2    def removeOccurrences(self, s: str, part: str) -> str:
3        n=len(part)
4        while part in s:
5            s=s.replace(part,"",1)
6        
7        return s
8            
9        