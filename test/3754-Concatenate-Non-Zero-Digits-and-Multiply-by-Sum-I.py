class Solution:
    def sumAndMultiply(self, n: int) -> int:
        s=str(n)
        st=0
        ans=""
        for i in s:
            if i!="0":
                ans+=i
                st+=int(i)
        if len(ans)==0:
            return 0
        return int(ans)*st
            

        