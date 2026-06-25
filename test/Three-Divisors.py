1class Solution:
2    def isThree(self, n: int) -> bool:
3        c=0
4        for i in range(1,int(n*0.5)+1):
5            if n%i==0:
6                c+=1
7                print(i)
8        c+=1
9        if c!=3:
10            return False
11        else:
12            return True
13        