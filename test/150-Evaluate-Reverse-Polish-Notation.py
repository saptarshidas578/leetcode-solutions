class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        l=[]
        for i in tokens:
            
            if i not in "+-*/":
                l.append(int(i))
            else:
                if i=="+":
                    l[-1]=l[-1]+l[-2]
                    if len(l)>=2:
                        l.pop(-2)
                elif i=="-":
                    l[-1]=l[-2]-l[-1]
                    if len(l)>=2:
                        l.pop(-2)
                elif i=="*":
                    l[-1]=l[-2]*l[-1]
                    if len(l)>=2:
                        l.pop(-2)
                else:
                    l[-1]=int(l[-2]/l[-1])
                    if len(l)>=2:
                        l.pop(-2)
                    
        return l[-1]

                
        