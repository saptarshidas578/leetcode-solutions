class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        def prod(n):
            p=1
            while n>0:
                p=p*(n%10)
                n=n//10
            return p
        
        while prod(n)%t!=0:
            n+=1
        else:
            return n
            
        
        

        