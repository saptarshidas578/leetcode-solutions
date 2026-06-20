1class Solution:
2    def corpFlightBookings(self, b: List[List[int]], n: int) -> List[int]:
3        l=[0]*(n+1)
4        for i in b:
5            x=i[0]
6            y=i[1]
7            l[x-1]+=i[-1]
8            l[y]-=i[-1]
9        
10        s=[]
11        for i in range(len(l)-1):
12            if i==0:
13                s.append(l[i])
14            else:
15                s.append(s[-1]+l[i])
16        return s
17
18        