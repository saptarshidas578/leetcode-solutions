1class Solution:
2    def reverseVowels(self, s: str) -> str:
3        vowels=[i for i in s if i in "aeiouAEIOU"]
4        result=[i if i not in "aeiouAEIOU" else vowels.pop() for i in s]
5        return "".join(result)