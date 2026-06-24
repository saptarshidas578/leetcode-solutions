1class Solution:
2    def merge(self, interval: List[List[int]]) -> List[List[int]]:
3        ans=[]
4        interval.sort()
5        interval.append(["",""])
6        old=interval[0][0]
7        new=interval[0][1]
8        for i in range(1,len(interval)):
9            if interval[i][0] in range(old,new+1):
10                if interval[i][1]>new:
11                    new= interval[i][1]
12            else:
13                ans.append([old,new])
14                old=interval[i][0]
15                new=interval[i][1]
16        return(ans)
17            
18        