1class Solution:
2    def convertToBase7(self, num: int) -> str:
3        n=num
4        num=abs(num)
5        rem=num%7
6        quo=num//7
7        l=[]
8        l.append(str(rem))
9        num=quo
10        while num!=0:
11            rem=num%7
12            quo=num//7
13            num=quo
14            l.append(str(rem))
15        #print(l)
16        l=l[::-1]
17        if n>=0:
18            return "".join(l)
19        else:
20            return "-"+"".join(l)
21
22
23
24        