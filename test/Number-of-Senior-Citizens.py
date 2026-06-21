1class Solution:
2    def countSeniors(self, details: List[str]) -> int:
3        n=0
4        for i in details:
5            if int(i[11:13])>60:
6                n+=1
7                #print(i)
8        return(n)
9        