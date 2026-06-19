1class Solution:
2    def largestAltitude(self, gain: List[int]) -> int:
3        l=[0]
4        gain.insert(0,0)
5        for i in range(1,len(gain)):
6            l.append(l[i-1]+gain[i])
7        return max(l)
8
9        