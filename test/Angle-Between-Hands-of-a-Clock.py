1class Solution:
2    def angleClock(self, hour: int, minutes: int) -> float:
3        hd=hour*30+minutes*0.5
4        md=6*minutes
5        diff = abs(hd-md)
6        odiff=abs(360-diff)
7        return min(diff,odiff)
8        
9        
10        