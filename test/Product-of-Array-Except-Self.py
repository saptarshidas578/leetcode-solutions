1class Solution:
2    from collections import Counter
3    def productExceptSelf(self, nums: List[int]) -> List[int]:
4        d=Counter(nums)
5        ans=[]
6        prod=1
7        print(d)
8        for i in nums:
9            for j in d:
10                if i==j and d[i]!=1:
11                    prod=prod*j**(d[j]-1)
12                elif i==j and d[i]==1:
13                    pass
14                else:
15                    prod=prod*j**d[j]
16            ans.append(prod)
17            print(prod)
18            prod=1
19        return(ans)
20        