class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        n = len(colors)
        summ, maxi, res = 0, 0, 0
        for i in range(n):
            if i > 0 and colors[i] != colors[i-1]:
                res += (summ - maxi)
                summ, maxi = 0, 0
            
            summ += neededTime[i]
            maxi = max(maxi, neededTime[i])
        res += (summ - maxi)
        
        return res
                