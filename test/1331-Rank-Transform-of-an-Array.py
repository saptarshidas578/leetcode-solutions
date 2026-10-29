class Solution:
    def arrayRankTransform(self, arr: list[int]) -> list[int]:
        s=list(set(arr))
        s.sort()
        d={}
        for i in range(1,len(s)+1):
            d[s[i-1]]=i
        for j in range(len(arr)):
            arr[j]=d[arr[j]]
        return(arr)


        