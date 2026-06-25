1class Solution:
2    from math import gcd
3    def gcdOfStrings(self, str1: str, str2: str) -> str:
4        if str1+str2!=str2+str1:
5            return ""
6        length=gcd(len(str1),len(str2))
7        return str1[:length]
8
9        