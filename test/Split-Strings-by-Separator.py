1class Solution:
2    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
3        l=[]
4        for i in words:
5            l.extend(i.split(separator))
6        l=[x for x in l if x!=""]
7        return l
8        