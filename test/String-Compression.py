1class Solution:
2    def compress(self, chars: List[str]) -> int:
3        l=deepcopy(chars)
4        chars.clear()
5        c=0
6        for i in range(0,len(l)-1):
7            if l[i]==l[i+1]:
8                c+=1
9            else:
10                chars.append(l[i])
11                c+=1
12                if c!=1:
13                    for j in str(c) :
14                        chars.append(j)
15                c=0
16        else:
17            chars.append(l[-1])
18            c+=1
19            if c!=1:
20                for j in str(c):
21                    chars.append(j)
22
23        print(chars)
24
25            
26
27
28        
29
30        