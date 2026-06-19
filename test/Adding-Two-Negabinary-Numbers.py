1class Solution:
2    def addNegabinary(self, arr1: List[int], arr2: List[int]) -> List[int]:
3        num1 = 0
4        num2 = 0
5
6        arr1 = arr1[::-1]
7        arr2 = arr2[::-1]
8
9        for i in range(len(arr1)):
10            num1 += arr1[i] * ((-2) ** i)
11
12        for i in range(len(arr2)):
13            num2 += arr2[i] * ((-2) ** i)
14
15        n = num1 + num2
16
17        if n == 0:
18            return [0]
19
20        ans = []
21
22        while n:
23            rem = n % -2
24            n //= -2
25
26            if rem < 0:
27                rem += 2
28                n += 1
29
30            ans.append(rem)
31
32        return ans[::-1]