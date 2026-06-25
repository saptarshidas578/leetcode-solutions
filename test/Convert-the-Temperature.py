1class Solution:
2    def convertTemperature(self, celsius: float) -> List[float]:
3        f=celsius*1.80+32
4        k=celsius+273.15
5        return [k,f]
6        