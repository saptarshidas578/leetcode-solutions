1class Solution:
2    def isHappy(self, n: int) -> bool:
3        def happy(n):
4            s=0
5            for i in n:
6                s=s+int(i)**2
7            return str(s)
8        n=str(n)
9        n=happy(n)
10        while True:
11            if n=="1"or n=="7":
12                return True
13            elif int(n)<10:
14                return False
15            else:
16                n=happy(n)
17            
18        