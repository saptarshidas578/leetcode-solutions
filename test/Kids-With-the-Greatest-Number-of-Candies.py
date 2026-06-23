1class Solution:
2    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
3        m=max(candies)
4        for i in range(len(candies)):
5            if candies[i]+extraCandies>=m:
6                candies[i]=True
7            else:
8                candies[i]=False
9        return candies
10
11        