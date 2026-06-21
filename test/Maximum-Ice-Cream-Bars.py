1class Solution:
2    def maxIceCream(self, costs: List[int], coins: int) -> int:
3        costs.sort()
4        s=0
5        c=0
6        for i in costs:
7            s+=i
8            if s>coins:
9                break
10            elif s==coins:
11                c+=1
12            else:
13                c+=1
14        return(c)
15        