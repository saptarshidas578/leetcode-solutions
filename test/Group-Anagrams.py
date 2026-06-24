1class Solution:
2    from collections import Counter
3    from collections import defaultdict
4
5    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
6        mp = defaultdict(list)
7
8        for word in strs:
9            key = tuple(sorted(word))  
10            mp[key].append(word)
11
12        return list(mp.values())
13
14
15
16
17        